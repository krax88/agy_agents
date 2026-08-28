---
name: analyze-large-audio
description: Uploads and processes large audio files (>20MB up to 2GB) using Gemini 3.7 Flash via the Files REST API. Preserves raw multimodal audio context, speaker distinction, emotion, and timestamps. Supported formats include .mp3, .wav, .flac, .aac, .m4a, .ogg, .opus, .webm, .aiff, .pcm.
---

# Large Audio Analysis Skill

Uploads and processes audio files of any size (up to 2GB) using the Gemini Files API resumable upload protocol and runs multimodal inference using `gemini-3.7-flash`.

## Supported Audio Formats & MIME Types

| Audio Format | File Extensions | MIME Type |
| :--- | :--- | :--- |
| **MP3** | `.mp3` | `audio/mp3` |
| **WAV** | `.wav` | `audio/wav` |
| **FLAC** | `.flac` | `audio/flac` |
| **AAC** | `.aac` | `audio/aac` |
| **M4A** | `.m4a` | `audio/m4a` |
| **OGG / Vorbis / Opus** | `.ogg`, `.opus` | `audio/ogg` |
| **WebM Audio** | `.webm` | `audio/webm` |
| **AIFF** | `.aiff`, `.aif` | `audio/aiff` |
| **PCM** | `.pcm` | `audio/pcm` |

## Execution

### 1. Upload & Analyze New Audio
Run the script to upload a local audio file and perform initial analysis:

```bash
.agents/skills/analyze-large-audio/scripts/gemini_audio_rest.sh "<path_to_audio_file>" "<instruction_prompt>" "[model]"
```

### 2. Query Existing Uploaded Audio (Zero-Upload Overhead)
Files remain available on Google's Files API for **48 hours**. Query an already-uploaded audio file by File ID, File URI, or Display Name without re-uploading:

```bash
.agents/skills/analyze-large-audio/scripts/query_existing_audio.sh "<file_id_or_display_name>" "<instruction_prompt>" "[model]"
```

### Parameters
- `<path_to_audio_file>`: Path to local audio file (`.mp3`, `.wav`, `.flac`, `.aac`, `.m4a`, `.ogg`, `.opus`, `.webm`, `.aiff`, `.pcm`).
- `<file_id_or_display_name>`: File ID (e.g. `files/abc123xyz`), resource URI, or original file name (e.g. `Ny inspelning 4.m4a`).
- `<instruction_prompt>`: Instruction/question for analyzing the audio (e.g., transcription, speaker diarization, executive summary, sentiment analysis).
- `[model]`: (Optional) Model name. Defaults to `gemini-3.7-flash`.

### Requirements
- Environment variable `GEMINI_API_KEY` must be set.
- `curl` and `jq` installed on the host system.

