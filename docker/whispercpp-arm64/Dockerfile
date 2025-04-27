FROM --platform=linux/arm64 ubuntu:22.04

RUN apt-get update && apt-get install -y git build-essential cmake ffmpeg wget python3 python3-pip && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/ggerganov/whisper.cpp.git /whisper.cpp
WORKDIR /whisper.cpp
RUN make

COPY transcribe.sh /app/transcribe.sh
WORKDIR /app

ENTRYPOINT ["bash", "transcribe.sh"]
