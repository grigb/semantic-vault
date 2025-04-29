FROM python:3.10-slim
WORKDIR /app
COPY server.py .
RUN pip install --no-cache-dir fastapi uvicorn sentence-transformers
EXPOSE 8080
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
