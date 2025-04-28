# User Journey: Integration with External Tools

- **Persona/Role:** Developer, integrator, power user
- **Journey Name:** Integration with External Tools
- **Related Features/Docs:**
  - [AnythingLLM Integration](../onboarding/SYSTEM_OVERVIEW.md)
  - [Obsidian/Notion Guides](../guides/Obsidian%20Gitcrypt%20Guide.md)
  - [Embedding Proxy API](../../README.md)
- **Preconditions:**
  - Platform is running and healthy
  - External tool (e.g., Obsidian, AnythingLLM) is installed/configured
- **Goal/Outcome:** Successfully connect an external tool, sync data, and verify round-trip integration

---

## Step-by-Step Journey

1. **Configure External Tool**
   - Set up API keys, endpoints, or plugins in the external tool (e.g., point AnythingLLM to Graphiti or Embedding Proxy)
2. **Initiate Data Sync or Ingestion**
   - Use the external tool’s UI or API to send data to the platform (e.g., export from Obsidian, upload to AnythingLLM)
3. **Verify Data Ingestion**
   - Confirm data appears in the platform (search, UI, or logs)
4. **Perform Semantic Actions**
   - Run a search, Q&A, or other workflow using the ingested data
5. **Test Round-Trip Integration**
   - Send results or updates back to the external tool if supported (e.g., sync annotations, export search results)

---

## Edge Cases & Variations
- API key or endpoint misconfiguration
- Data format incompatibility
- Partial/incomplete sync
- Version mismatch between tools

---

## Expected Results
- External tool connects and syncs with the platform
- Data flows in both directions (if supported)
- Errors are reported and do not cause data loss

---

## Testing Checklist
- [ ] External tool can connect to platform
- [ ] Data can be sent from tool to platform
- [ ] Ingested data is accessible in platform
- [ ] Semantic actions work on new data
- [ ] (If supported) Updates flow back to tool
- [ ] Errors are handled gracefully

---

## Feedback & Improvements
- Report integration issues via GitHub Issues or project chat
- Suggest improvements to this journey doc via pull request
