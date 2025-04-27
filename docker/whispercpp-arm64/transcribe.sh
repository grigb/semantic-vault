#!/bin/bash
# Usage: docker run ... /data/sample.wav

AUDIO_FILE="$1"
MODEL_PATH="/whisper.cpp/models/ggml-base.en.bin"

if [ ! -f "$MODEL_PATH" ]; then
  mkdir -p /whisper.cpp/models
  wget -O "$MODEL_PATH" https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base.en.bin
fi

/whisper.cpp/whisper -m "$MODEL_PATH" -f "$AUDIO_FILE" -of /app/output.txt
cat /app/output.txt
