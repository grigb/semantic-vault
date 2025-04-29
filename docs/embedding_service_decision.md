# Embedding Service Decision Record

**Date:** 2025-04-28

## Summary
After reviewing project documentation and requirements, we have made the following architectural decision regarding the embedding service for the Semantic Vault system.

## Decision
- **Service Chosen:** LocalAI (https://github.com/go-skynet/local-ai)
- **Rationale:**
  - Free and open source.
  - Runs in a Docker container (ARM64 and x86 support).
  - Fast for text embeddings using models like `all-MiniLM-L6-v2`.
  - Exposes an OpenAI-compatible API (`/v1/embeddings`) for seamless integration with our backend.
  - Supports Sentence Transformers and other community models.
  - Actively maintained, easy to extend, and well-documented.
- **Alternatives Considered:**
  - Sentence Transformers server (requires more manual setup, but can be used via LocalAI).
  - Weaviate multi2vec-clip (better for multimodal/image, not needed for current text use case).
  - Whisper (audio, not relevant for current needs).

## Implementation Plan
1. **Add LocalAI to Docker Compose:**
   - Use the official image: `quay.io/go-skynet/local-ai:latest`
   - Expose on port 9009 (maps to 8080 in container)
   - Mount a `./models` directory for model storage
2. **Configure LocalAI to load `all-MiniLM-L6-v2` by default** (or another fast, free model)
3. **Update backend and documentation to use `host.docker.internal:9009` as the embedding endpoint**
4. **Test integration and update automated tests to ensure full coverage**

## Next Steps
- Update Docker Compose and spin up LocalAI
- Download and configure `all-MiniLM-L6-v2` model in the `./models` directory
- Verify API connectivity and run backend tests

---

*This document records the rationale and plan for embedding service integration. All future changes or alternatives should reference this decision for traceability.*
