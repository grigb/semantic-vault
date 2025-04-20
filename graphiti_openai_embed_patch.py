import os
import requests

class PatchedOpenAIEmbedder:
    def __init__(self, api_base=None):
        # Use the local proxy endpoint
        self.api_base = api_base or os.environ.get("OPENAI_API_BASE", "http://host.docker.internal:9009/v1")
        self.api_key = os.environ.get("OPENAI_API_KEY", "dummy-key")

    async def create(self, input_data):
        # input_data is a list of strings
        payload = {
            "model": "local-embedding-model",
            "input": input_data
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(f"{self.api_base}/embeddings", json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        # Return in the format expected by Graphiti
        return data
