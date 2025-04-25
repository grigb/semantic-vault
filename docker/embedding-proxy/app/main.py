from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import torch
from typing import List
import threading

app = FastAPI()

# Thread-safe model cache
model_cache = {}
model_cache_lock = threading.Lock()

# Default model
DEFAULT_MODEL_NAME = "all-MiniLM-L6-v2"

# Load default model at startup
with model_cache_lock:
    model_cache[DEFAULT_MODEL_NAME] = SentenceTransformer(DEFAULT_MODEL_NAME)

def get_model(model_name: str):
    with model_cache_lock:
        if model_name not in model_cache:
            try:
                model_cache[model_name] = SentenceTransformer(model_name)
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Could not load model '{model_name}': {e}")
        return model_cache[model_name]

def compute_embeddings(texts, model_name=DEFAULT_MODEL_NAME):
    model = get_model(model_name)
    with torch.no_grad():
        return model.encode(texts, convert_to_numpy=True).tolist()

class EmbeddingRequest(BaseModel):
    input: List[str]
    model: str = DEFAULT_MODEL_NAME

class InstallModelRequest(BaseModel):
    model: str

@app.get("/v1/models")
def list_models():
    """List models currently loaded in memory."""
    with model_cache_lock:
        return {"loaded_models": list(model_cache.keys())}

@app.post("/v1/install_model")
def install_model(req: InstallModelRequest):
    """Download and cache a new model by name."""
    model_name = req.model
    try:
        get_model(model_name)
        return {"status": "ok", "model": model_name}
    except HTTPException as e:
        raise e

@app.post("/v1/embeddings")
def create_embeddings(req: EmbeddingRequest):
    if not req.input or not isinstance(req.input, list):
        raise HTTPException(status_code=400, detail="Input must be a non-empty list of strings.")
    vectors = compute_embeddings(req.input, model_name=req.model)
    return {
        "object": "list",
        "data": [
            {"object": "embedding", "embedding": vec, "index": i} for i, vec in enumerate(vectors)
        ],
        "model": req.model,
        "usage": {"prompt_tokens": sum(len(t.split()) for t in req.input), "total_tokens": sum(len(t.split()) for t in req.input)}
    }

# API Documentation (for README):
# - GET /v1/models: List loaded models
# - POST /v1/install_model {"model": "model_name"}: Download/install a new model
# - POST /v1/embeddings {"input": [...], "model": "model_name"}: Use a specific model for embedding
