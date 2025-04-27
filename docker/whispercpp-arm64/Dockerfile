FROM --platform=linux/arm64 ubuntu:22.04

RUN apt-get update && apt-get install -y git build-essential cmake ffmpeg wget python3 python3-pip && rm -rf /var/lib/apt/lists/*

RUN git clone --branch master https://github.com/ggerganov/whisper.cpp.git /whisper.cpp \
    && ls -lh /whisper.cpp \
    && if [ ! -f /whisper.cpp/Makefile ]; then echo 'ERROR: Makefile missing after clone!'; ls -lah /whisper.cpp; exit 1; fi
WORKDIR /whisper.cpp
RUN make V=1 || make -C build V=1 \
    && ls -lR /whisper.cpp
RUN if [ -f /whisper.cpp/whisper ]; then cp /whisper.cpp/whisper /whisper.cpp/main; elif [ -f /whisper.cpp/build/whisper ]; then cp /whisper.cpp/build/whisper /whisper.cpp/main; fi

COPY transcribe.sh /app/transcribe.sh
WORKDIR /app

ENTRYPOINT ["bash", "transcribe.sh"]
