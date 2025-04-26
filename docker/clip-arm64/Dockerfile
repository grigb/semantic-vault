FROM --platform=linux/arm64 python:3.10-slim

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN pip install torch torchvision open_clip_torch pillow

COPY embed_image.py /app/embed_image.py
WORKDIR /app

ENTRYPOINT ["python", "embed_image.py"]
