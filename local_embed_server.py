from fastapi import FastAPI, Request
from sentence_transformers import SentenceTransformer
import torch
import uvicorn

app = FastAPI()

# Use MPS (Apple Silicon GPU) if available, otherwise CPU
device = "mps" if torch.backends.mps.is_available() else "cpu"
model = SentenceTransformer('all-MiniLM-L6-v2', device=device)

@app.post("/embeddings")
async def embed(request: Request):
    data = await request.json()
    sentences = data.get("sentences", [])
    embeddings = model.encode(sentences).tolist()
    return {"embeddings": embeddings}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9008)
