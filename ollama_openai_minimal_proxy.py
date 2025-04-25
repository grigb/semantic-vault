import threading
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional, Union
from sentence_transformers import SentenceTransformer
import numpy as np

# Load the embedding model once at startup (thread-safe)
MODEL_NAME = "all-MiniLM-L6-v2"
_model_lock = threading.Lock()
_model = None

def get_model():
    global _model
    with _model_lock:
        if _model is None:
            _model = SentenceTransformer(MODEL_NAME)
        return _model

app = FastAPI()

class EmbeddingRequest(BaseModel):
    model: Optional[str] = None
    input: Union[str, List[str]]

import traceback
from fastapi.responses import JSONResponse

@app.post("/v1/embeddings")
def v1_embeddings(req: EmbeddingRequest):
    try:
        # Accept both string and list input
        if isinstance(req.input, str):
            texts = [req.input]
        else:
            texts = req.input
        model = get_model()
        vectors = model.encode(texts, show_progress_bar=False, normalize_embeddings=True)
        # Ensure vectors is always a list of lists
        if isinstance(vectors, np.ndarray):
            vectors = vectors.tolist()
        elif isinstance(vectors, list) and isinstance(vectors[0], np.ndarray):
            vectors = [v.tolist() for v in vectors]
        # Ensure that for a single input string, vectors is a list of one vector
        # and for multiple input strings, vectors is a list of vectors
        response = {
            "object": "list",
            "data": [
                {
                    "object": "embedding",
                    "index": i,
                    "embedding": vec.tolist() if hasattr(vec, 'tolist') else list(vec)
                }
                for i, vec in enumerate(vectors)
            ],
            "model": req.model or MODEL_NAME,
            "usage": {"prompt_tokens": 0, "total_tokens": 0}
        }
        print('EMBEDDING RESPONSE:', response)
        return response
    except Exception as e:
        tb = traceback.format_exc()
        print(f"[ERROR] Exception in /v1/embeddings: {e}\n{tb}")
        return JSONResponse(status_code=500, content={"error": str(e), "traceback": tb})


@app.get("/")
def root():
    return {"status": "ok", "proxy": "local-sentence-transformers"}
