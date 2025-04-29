from fastapi import FastAPI, Request
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from typing import List
import uvicorn

app = FastAPI()
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

class EmbeddingRequest(BaseModel):
    input: List[str]
    model: str = "all-MiniLM-L6-v2"

@app.post("/v1/embeddings")
def create_embedding(req: EmbeddingRequest):
    vectors = model.encode(req.input, convert_to_numpy=True).tolist()
    return {
        "object": "list",
        "data": [
            {"object": "embedding", "embedding": v, "index": i}
            for i, v in enumerate(vectors)
        ],
        "model": req.model,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
