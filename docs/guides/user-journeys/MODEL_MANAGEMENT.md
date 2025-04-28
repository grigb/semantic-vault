# User Journey: Model Management

- **Persona/Role:** Admin, advanced user, developer
- **Journey Name:** Model Management
- **Related Features/Docs:**
  - [Model Catalog API Design](../../design-docs/MODEL_CATALOG_API_DESIGN.md)
  - [Master Checklist](../../planning/SEMANTIC_SYSTEM_MASTER_CHECKLIST.md)
  - [Onboarding & First Run](./ONBOARDING_FIRST_RUN.md)
- **Preconditions:**
  - Platform is running and healthy
  - User has admin or model management permissions
- **Goal/Outcome:** List, install, and switch embedding/LLM models; verify persistence across restarts

---

## Step-by-Step Journey

1. **List Available Models**
   - Use the API or UI to list all local and remote models (e.g., `/api/v1/models`)
   - Confirm metadata (name, type, description, status) is displayed
2. **Install a New Model**
   - Trigger model installation via API/UI (e.g., select from Hugging Face or local path)
   - Wait for install to complete and verify status
3. **Switch Active Model**
   - Use API/UI to set a different model as active for embeddings or LLM
   - Confirm the switch is reflected in the system (status, logs, or UI)
4. **Verify Model Persistence**
   - Restart relevant containers/services
   - List models again and verify installed models and active status persist
5. **Error Handling**
   - Attempt to install an invalid or duplicate model and verify error reporting

---

## Edge Cases & Variations
- Network failure during remote model install
- Insufficient disk space
- Switching to an incompatible model type
- Model metadata missing or incorrect

---

## Expected Results
- Models can be listed, installed, and switched without error
- Model state persists across container/service restarts
- Errors are reported clearly and do not affect other models

---

## Testing Checklist
- [ ] Models are listed with correct metadata
- [ ] New models can be installed and appear in the list
- [ ] Active model can be switched and used
- [ ] Model state persists after restart
- [ ] Errors are handled gracefully

---

## Feedback & Improvements
- Report model management issues via GitHub Issues or project chat
- Suggest improvements to this journey doc via pull request
