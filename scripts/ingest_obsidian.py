#!/usr/bin/env python3
"""
ingest_obsidian.py: Read Obsidian markdown notes, embed them with OpenAI,
store vectors in Qdrant, extract semantic triples with OpenAI,
and send triples to Graphiti.
"""
import os
import glob
import json
import requests
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
import openai

def main():
    # Load environment variables from project .env
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

    # Config
    OBSIDIAN_VAULT = os.getenv('OBSIDIAN_VAULT_PATH', 'obsidian-vault')  # Path to Obsidian vault directory
    QDRANT_HOST = os.getenv('QDRANT_HOST', 'localhost')
    QDRANT_PORT = int(os.getenv('QDRANT_PORT', '9004'))
    GRAPHITI_API_URL = os.getenv('GRAPHITI_API_URL', 'http://localhost:9003')
    GRAPHITI_API_KEY = os.getenv('GRAPHITI_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    # Validate API keys
    if not OPENAI_API_KEY or OPENAI_API_KEY.lower() in ('', 'unused'):
        print('ERROR: OPENAI_API_KEY is not set or is default. Please update .env with your OpenAI API key.')
        exit(1)
    if not GRAPHITI_API_KEY:
        print('ERROR: GRAPHITI_API_KEY is not set. Please update .env with your Graphiti API key.')
        exit(1)

    # Initialize clients
    openai.api_key = OPENAI_API_KEY
    qdrant = QdrantClient(url=f"http://{QDRANT_HOST}", port=QDRANT_PORT)

    # Discover and process markdown files
    base_dir = os.path.join(os.path.dirname(__file__), '..', OBSIDIAN_VAULT)
    md_files = glob.glob(os.path.join(base_dir, '**', '*.md'), recursive=True)

    for path in md_files:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()

        # 1. Generate embedding and upsert into Qdrant
        emb = openai.embeddings.create(model='text-embedding-ada-002', input=text)
        vector = emb['data'][0]['embedding']
        point = PointStruct(id=path, vector=vector, payload={'path': path})
        qdrant.upsert(collection_name='obsidian', points=[point])
        print(f"Indexed: {path}")

        # 2. Extract semantic triples via ChatCompletion
        prompt = (
            "Extract semantic triples (subject, predicate, object) from the following text."
            f"\n\nText:\n{text}\n\nReturn JSON list of triples, e.g. [[\"S\", \"P\", \"O\"], ...]"
        )
        chat = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'system', 'content': 'You extract semantic triples from text.'},
                      {'role': 'user', 'content': prompt}],
            temperature=0
        )
        try:
            triples = json.loads(chat.choices[0].message.content)
        except Exception:
            print(f"Failed parsing triples for {path}")
            continue

        # 3. Send triples to Graphiti
        url = f"{GRAPHITI_API_URL}/triples"
        headers = {'Authorization': f'Bearer {GRAPHITI_API_KEY}'}
        res = requests.post(url, json={'triples': triples}, headers=headers)
        if res.ok:
            print(f"Sent triples for {path}")
        else:
            print(f"Error sending {path}: {res.status_code}")

if __name__ == '__main__':
    main()
