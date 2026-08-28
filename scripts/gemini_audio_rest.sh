#!/usr/bin/env bash
set -e

FILE_PATH="$1"
PROMPT="$2"
MODEL="${3:-gemini-3.7-flash}"

if [ -z "$FILE_PATH" ] || [ -z "$PROMPT" ]; then
  echo "Usage: $0 <path_to_audio_file> <instruction_prompt> [model]"
  exit 1
fi

if [ -z "$GEMINI_API_KEY" ]; then
  echo "Error: GEMINI_API_KEY environment variable is not set."
  exit 1
fi

if [ ! -f "$FILE_PATH" ]; then
  echo "Error: File '$FILE_PATH' not found."
  exit 1
fi

# Detect File Extension
EXT="${FILE_PATH##*.}"
EXT_LOWER=$(echo "$EXT" | tr '[:upper:]' '[:lower:]')

# Map and validate allowed file types to official Gemini MIME types
case "$EXT_LOWER" in
  mp3)
    MIME_TYPE="audio/mp3"
    ;;
  wav)
    MIME_TYPE="audio/wav"
    ;;
  flac)
    MIME_TYPE="audio/flac"
    ;;
  aac)
    MIME_TYPE="audio/aac"
    ;;
  m4a)
    MIME_TYPE="audio/m4a"
    ;;
  ogg|opus)
    MIME_TYPE="audio/ogg"
    ;;
  webm)
    MIME_TYPE="audio/webm"
    ;;
  aiff|aif)
    MIME_TYPE="audio/aiff"
    ;;
  pcm)
    MIME_TYPE="audio/pcm"
    ;;
  *)
    echo "Error: Unsupported audio format '.$EXT_LOWER'."
    echo "Allowed formats: .mp3, .wav, .flac, .aac, .m4a, .ogg, .opus, .webm, .aiff, .pcm"
    exit 1
    ;;
esac

NUM_BYTES=$(wc -c < "$FILE_PATH" | tr -d ' ')
DISPLAY_NAME=$(basename "$FILE_PATH")

# 1. Resumable Upload Handshake
INIT_RESPONSE=$(curl -s -i -X POST "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{\"file\": {\"display_name\": \"${DISPLAY_NAME}\"}}")

UPLOAD_URL=$(echo "$INIT_RESPONSE" | grep -i "^x-goog-upload-url:" | awk '{print $2}' | tr -d '\r')

if [ -z "$UPLOAD_URL" ]; then
  echo "Error: Failed to obtain upload URL from Gemini Files API."
  echo "$INIT_RESPONSE"
  exit 1
fi

# 2. Upload Raw Binary Audio Chunks (Supports up to 2GB)
UPLOAD_RESULT=$(curl -s -X POST "$UPLOAD_URL" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary @"$FILE_PATH")

FILE_URI=$(echo "$UPLOAD_RESULT" | jq -r '.file.uri')

if [ "$FILE_URI" = "null" ] || [ -z "$FILE_URI" ]; then
  echo "Error: Failed to upload file bytes."
  echo "$UPLOAD_RESULT"
  exit 1
fi

# 3. Call generateContent on gemini-3.7-flash with File URI reference
REQUEST_BODY=$(jq -n \
  --arg uri "$FILE_URI" \
  --arg mime "$MIME_TYPE" \
  --arg prompt "$PROMPT" \
  '{
    contents: [
      {
        parts: [
          { fileData: { mimeType: $mime, fileUri: $uri } },
          { text: $prompt }
        ]
      }
    ]
  }')

GEN_RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent?key=${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$REQUEST_BODY")

echo "$GEN_RESPONSE" | jq -r '.candidates[0].content.parts[0].text // .error.message'
