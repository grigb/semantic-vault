#!/usr/bin/env python3
"""
quick_ingest_neo4j.py: Minimal script to create test nodes and a SIMILAR_TO relationship with a 1536-dim embedding vector in Neo4j for vector search testing.
"""
from datetime import datetime, timezone
import os
import requests
from neo4j import GraphDatabase

NEO4J_URI = os.getenv('NEO4J_URI', 'bolt://localhost:9007')
NEO4J_USER = os.getenv('NEO4J_USER', 'neo4j')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

VECTOR_DIM = 1536
EMBEDDING_PROXY_URL = os.getenv('EMBEDDING_PROXY_URL', 'http://localhost:9009/v1/embeddings')


def get_embedding(text: str):
    resp = requests.post(EMBEDDING_PROXY_URL, json={"input": [text]})
    resp.raise_for_status()
    return resp.json()['data'][0]['embedding']


def main():
    if not NEO4J_PASSWORD:
        print('ERROR: NEO4J_PASSWORD not set in environment.')
        exit(1)
    embedding = get_embedding("test fact")
    created_at = datetime.now(timezone.utc).isoformat()
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    with driver.session() as session:
        # Clean up previous test data
        session.run("MATCH (a:Entity)-[r:RELATES_TO]->(b:Entity) DETACH DELETE a, b")
        # Create nodes and relationship with fact_embedding and created_at
        session.run(
            """
            CREATE (a:Entity {name: 'NodeA', uuid: 'entity-uuid-a', group_id: 'products'})-[:RELATES_TO {
                fact_embedding: $embedding,
                fact: 'Vector search test fact',
                name: 'Test Fact',
                uuid: 'test-uuid-1',
                file_path: 'test.md',
                group_id: 'products',
                created_at: datetime($created_at),
                episodes: $episodes
            }]->(b:Entity {name: 'NodeB', uuid: 'entity-uuid-b', group_id: 'products'})
            """,
            embedding=embedding,
            created_at=created_at,
            episodes=[]
        )
    print('Test Entity nodes and RELATES_TO relationship with real fact_embedding and created_at created.')

if __name__ == '__main__':
    main()
