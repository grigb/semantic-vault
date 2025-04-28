# User Journey: Advanced Search & Filtering

- **Persona/Role:** Power user, developer, researcher
- **Journey Name:** Advanced Search & Filtering
- **Related Features/Docs:**
  - [Search API](../../README.md#running-searches)
  - [Graphiti API Docs](../../graphiti/README.md)
  - [Semantic Search Journey](./SEMANTIC_SEARCH.md)
- **Preconditions:**
  - Platform is running and healthy
  - Data is ingested and accessible
- **Goal/Outcome:** Perform advanced searches using query parameters, group IDs, and filters; handle edge cases

---

## Step-by-Step Journey

1. **Prepare Advanced Search Query**
   - Include parameters such as group_ids, filters, or custom limits
   - Example: `{ "query": "project update", "group_ids": ["engineering"], "max_facts": 20, "filters": {"created_after": "2024-01-01"} }`
2. **Send Search Request**
   - Use API, UI, or script to POST to `/search` with advanced parameters
3. **Interpret Results**
   - Verify results are filtered and grouped as expected
4. **Test Edge Cases**
   - Submit queries with no matching results (empty)
   - Test large queries (pagination, limits)
   - Submit malformed or invalid queries (error handling)
5. **Adjust and Repeat**
   - Modify parameters to explore different scenarios

---

## Edge Cases & Variations
- No results returned
- Invalid or unsupported filter parameters
- Large result sets (pagination/limits)
- Query timeouts or performance issues

---

## Expected Results
- Results are filtered/grouped as specified
- Edge cases are handled gracefully (empty, invalid, large)
- Errors are reported clearly

---

## Testing Checklist
- [ ] Advanced parameters are accepted by the API
- [ ] Results are filtered/grouped as expected
- [ ] Empty and invalid queries are handled gracefully
- [ ] Large queries are paginated or limited
- [ ] Errors are reported clearly

---

## Feedback & Improvements
- Report advanced search issues via GitHub Issues or project chat
- Suggest improvements to this journey doc via pull request
