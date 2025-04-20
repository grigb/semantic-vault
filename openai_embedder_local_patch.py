"""
Patched OpenAIEmbedder for local embedding server
"""
"""
Patched OpenAIEmbedder for local embedding server ONLY. No OpenAI SDK calls remain.
"""
from collections.abc import Iterable
import requests
from .client import EmbedderClient, EmbedderConfig

DEFAULT_EMBEDDING_MODEL = 'text-embedding-3-small'

class OpenAIEmbedderConfig(EmbedderConfig):
    embedding_model: str = DEFAULT_EMBEDDING_MODEL
    api_key: str | None = None
    base_url: str | None = None

class OpenAIEmbedder(EmbedderClient):
    """
    Fully patched Embedder Client that ONLY calls the local embedding proxy.
    """
    def __init__(self, config: OpenAIEmbedderConfig | None = None, client=None):
        if config is None:
            config = OpenAIEmbedderConfig()
        self.config = config
        self.api_key = config.api_key or "dummy-key"
        self.base_url = config.base_url or "http://host.docker.internal:9009/v1"

    async def create(self, input_data: str | list[str] | Iterable[int] | Iterable[Iterable[int]]) -> list[float]:
        # Always send a list of strings
        if isinstance(input_data, str):
            sentences = [input_data]
        else:
            sentences = list(input_data)
        payload = {
            "model": self.config.embedding_model,
            "input": sentences
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        # Call the local proxy (blocking call in async context is safe for this patch)
        response = requests.post(f"{self.base_url}/embeddings", json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        # Return the first embedding (Graphiti expects a single vector)
        return data["data"][0]["embedding"]
