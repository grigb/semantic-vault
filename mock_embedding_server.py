from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class EmbeddingRequest(BaseModel):
    input: List[str]
    model: str = "mock-model"

@app.post("/v1/embeddings")
def create_embeddings(req: EmbeddingRequest):
    # Return a fake embedding for each input
    return {
        "data": [
            {"embedding": [0.1] * 384, "index": idx} for idx, _ in enumerate(req.input)
        ],
        "model": req.model,
        "object": "list"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9009)
