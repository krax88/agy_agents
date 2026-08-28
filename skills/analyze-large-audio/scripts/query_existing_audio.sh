#!/usr/bin/env bash
set -e

FILE_IDENTIFIER="$1"
PROMPT="$2"
MODEL="${3:-gemini-3.7-flash}"

if [ -z "$FILE_IDENTIFIER" ] || [ -z "$PROMPT" ]; then
  echo "Usage: $0 <file_id_or_display_name> <prompt> [model]"
  exit 1
fi

if [ -z "$GEMINI_API_KEY" ]; then
  echo "Error: GEMINI_API_KEY environment variable is not set."
  exit 1
fi

# 1. Normalize resource name (e.g., handles 'files/abc', 'abc', or URL)
if [[ "$FILE_IDENTIFIER" =~ ^https://generativelanguage.googleapis.com/v1beta/(files/[a-zA-Z0-9_-]+) ]]; then
  FILE_RESOURCE="${BASH_REMATCH[1]}"
elif [[ "$FILE_IDENTIFIER" =~ ^files/ ]]; then
  FILE_RESOURCE="$FILE_IDENTIFIER"
elif [[ "$FILE_IDENTIFIER" =~ ^[a-zA-Z0-9_-]+$ ]] && [ ${#FILE_IDENTIFIER} -gt 8 ]; then
  FILE_RESOURCE="files/$FILE_IDENTIFIER"
else
  FILE_RESOURCE=""
fi

# 2. Fetch File Metadata
if [ -n "$FILE_RESOURCE" ]; then
  FILE_INFO=$(curl -s "https://generativelanguage.googleapis.com/v1beta/${FILE_RESOURCE}?key=${GEMINI_API_KEY}")
fi

# If not found directly by ID, search active files by display name
if [ -z "$FILE_RESOURCE" ] || echo "$FILE_INFO" | jq -e '.error' > /dev/null 2>&1; then
  ALL_FILES=$(curl -s "https://generativelanguage.googleapis.com/v1beta/files?key=${GEMINI_API_KEY}")
  MATCHED_RESOURCE=$(echo "$ALL_FILES" | jq -r --arg query "$FILE_IDENTIFIER" '.files[] | select(.displayName == $query or .name == $query) | .name' | head -n 1)
  
  if [ -n "$MATCHED_RESOURCE" ]; then
    FILE_RESOURCE="$MATCHED_RESOURCE"
    FILE_INFO=$(curl -s "https://generativelanguage.googleapis.com/v1beta/${FILE_RESOURCE}?key=${GEMINI_API_KEY}")
  else
    echo "Error: File '$FILE_IDENTIFIER' not found in active Files API storage."
    exit 1
  fi
fi

FILE_URI=$(echo "$FILE_INFO" | jq -r '.uri // empty')
MIME_TYPE=$(echo "$FILE_INFO" | jq -r '.mimeType // empty')
STATE=$(echo "$FILE_INFO" | jq -r '.state // empty')

if [ "$STATE" != "ACTIVE" ]; then
  echo "Error: File is in state '$STATE' (must be ACTIVE)."
  exit 1
fi

# 3. Query gemini-3.7-flash instantly using the existing file URI
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

OUTPUT_TEXT=$(echo "$GEN_RESPONSE" | jq -r '.candidates[0].content.parts[0].text // empty')

if [ -n "$OUTPUT_TEXT" ]; then
  echo "$OUTPUT_TEXT"
else
  echo "API Error:"
  echo "$GEN_RESPONSE" | jq -r '.error.message // .'
fi
