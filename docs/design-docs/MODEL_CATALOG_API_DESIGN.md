# Model Catalog API Design

---

## Purpose
To provide a unified API for listing, searching, and managing both local and remote (Hugging Face, etc.) models for use in the semantic/LLM system. This API is foundational for model management, selection, installation, and switching in both the backend and web UI.

---

## Requirements
- List all locally available models (embedding and LLMs)
- List/search remote models from Hugging Face (filter by type, e.g., SentenceTransformers, LLMs)
- Provide metadata: name, type (embedding/LLM), description, size, source, install status
- Support pagination and filtering
- Return results in a format suitable for UI consumption
- Extensible for future providers (Ollama, LM Studio, etc.)

---

## API Endpoints

### OpenAPI Spec (YAML)

```yaml
openapi: 3.0.3
info:
  title: Model Catalog API
  version: 1.0.0
paths:
  /v1/model_catalog:
    get:
      summary: List models (local and remote)
      parameters:
        - in: query
          name: source
          schema:
            type: string
            enum: [local, huggingface, all]
          description: Source of models (default: all)
        - in: query
          name: type
          schema:
            type: string
            enum: [embedding, llm, all]
          description: Model type (default: all)
        - in: query
          name: search
          schema:
            type: string
          description: Fuzzy search string
        - in: query
          name: page
          schema:
            type: integer
            default: 1
          description: Page number
        - in: query
          name: page_size
          schema:
            type: integer
            default: 20
          description: Results per page
      responses:
        '200':
          description: List of models
          content:
            application/json:
              schema:
                type: object
                properties:
                  models:
                    type: array
                    items:
                      $ref: '#/components/schemas/ModelMetadata'
                  page:
                    type: integer
                  total:
                    type: integer
components:
  schemas:
    ModelMetadata:
      type: object
      properties:
        name:
          type: string
        type:
          type: string
          enum: [embedding, llm]
        description:
          type: string
        size:
          type: string
        source:
          type: string
        installed:
          type: boolean
```

---

### Local Model Cache Directory Structure & Metadata Extraction

- **Directory Structure:**
  - All local models are stored in a configurable cache directory, e.g. `~/.semantic_models/`.
  - Subdirectories for each model: `<cache_dir>/<model_name>/`
  - Each model directory contains:
    - Model files (weights, configs)
    - `metadata.json` (containing: name, type, description, size, source, install date, etc.)
- **Metadata Extraction:**
  - On API request, scan the cache directory for all subdirectories.
  - Read and parse `metadata.json` for each model.
  - If `metadata.json` is missing, attempt to infer metadata from file names or directory structure.
  - Compute size from disk usage if not specified.
  - Mark `installed: true` for all models found locally.
- **Extensibility:**
  - Future providers (Ollama, LM Studio) should follow the same pattern: adapter writes compatible `metadata.json`.

---

All requirements and acceptance criteria from the [Phase 2 checklist](../planning/SEMANTIC_SYSTEM_MASTER_CHECKLIST.md) are now addressed in this design. See also:
- [../SEMANTIC_SYSTEM_STRATEGY.md](../SEMANTIC_SYSTEM_STRATEGY.md)
- [../SEMANTIC_SYSTEM_FULL_VISION.md](../SEMANTIC_SYSTEM_FULL_VISION.md)

## Model Metadata Schema
- `name` (string)
- `type` (string: `embedding` | `llm`)
- `description` (string)
- `size` (string, e.g., "80MB", "13GB")
- `source` (string: `local`, `huggingface`, etc.)
- `installed` (bool)

---

## Implementation Notes
- Local models: scan model cache directory, parse metadata
- Hugging Face: use [huggingface_hub](https://huggingface.co/docs/huggingface_hub) API to search/filter
- Future: add other providers (Ollama, LM Studio) with adapters
- Should be thread-safe and cache remote results for performance

---

## Dependencies
- [huggingface_hub](https://pypi.org/project/huggingface-hub/)
- FastAPI
- Python 3.10+

---

## Related Docs
- [../SEMANTIC_SYSTEM_MASTER_CHECKLIST.md](../SEMANTIC_SYSTEM_MASTER_CHECKLIST.md)
- [../SEMANTIC_SYSTEM_STRATEGY.md](../SEMANTIC_SYSTEM_STRATEGY.md)
- [../SEMANTIC_SYSTEM_FULL_VISION.md](../SEMANTIC_SYSTEM_FULL_VISION.md)

---

## Next Steps
1. Prototype `/v1/model_catalog` endpoint (local + Hugging Face)
2. Define model cache directory structure and metadata extraction
3. Integrate with UI for model browsing/search/selection
4. Document usage and update onboarding
