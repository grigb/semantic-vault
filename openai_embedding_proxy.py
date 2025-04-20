from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
import os
import uvicorn
from typing import List, Optional

# Config
LOCAL_EMBEDDINGS_URL = os.environ.get("LOCAL_EMBEDDINGS_URL", "http://localhost:9008/embeddings")

app = FastAPI()

class EmbeddingRequest(BaseModel):
    model: str
    input: List[str] | str
    user: Optional[str] = None

@app.post("/v1/embeddings")
async def openai_embeddings(req: EmbeddingRequest):
    # OpenAI allows both a single string or list of strings
    sentences = req.input if isinstance(req.input, list) else [req.input]
    # Forward to local server
    response = requests.post(
        LOCAL_EMBEDDINGS_URL,
        json={"sentences": sentences},
        timeout=30
    )
    response.raise_for_status()
    embeddings = response.json()["embeddings"]
    # Format as OpenAI
    return {
        "object": "list",
        "data": [
            {
                "object": "embedding",
                "index": i,
                "embedding": emb
            } for i, emb in enumerate(embeddings)
        ],
        "model": req.model,
        "usage": {"prompt_tokens": len(sentences), "total_tokens": len(sentences)}
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9009)
