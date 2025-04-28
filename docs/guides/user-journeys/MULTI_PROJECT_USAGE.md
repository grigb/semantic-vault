# User Journey: Multi-Project / Multi-Tenant Usage

- **Persona/Role:** Admin, advanced user, integrator
- **Journey Name:** Multi-Project / Multi-Tenant Usage
- **Related Features/Docs:**
  - [Development Guide](../onboarding/DEVELOPMENT_GUIDE.md)
  - [Master Checklist](../../planning/SEMANTIC_SYSTEM_MASTER_CHECKLIST.md)
  - [Onboarding & First Run](./ONBOARDING_FIRST_RUN.md)
- **Preconditions:**
  - Platform is running and healthy
  - User has permissions to create/manage projects or namespaces
- **Goal/Outcome:** Set up and switch between projects/namespaces, ensuring data and model isolation

---

## Step-by-Step Journey

1. **Create a New Project or Namespace**
   - Use the API/UI or Docker Compose to create a new project environment
   - Set up separate `.env` files, volumes, or config as needed
2. **Ingest Data into Each Project**
   - Add unique data to each project/namespace
   - Confirm data is only accessible within its own context
3. **Switch Between Projects**
   - Use UI, API, or Docker Compose to switch active project/namespace
   - Verify the active context changes and data/models are isolated
4. **Test Model Isolation**
   - Install/switch models in one project and verify no effect on others
5. **Simulate Multi-Tenant Access**
   - (If supported) Log in as different users/roles and verify access boundaries

---

## Edge Cases & Variations
- Accidental data/model leakage between projects
- Misconfiguration of environment variables or volumes
- Simultaneous access by multiple users

---

## Expected Results
- Projects/namespaces are isolated (data, models, configs)
- Switching is seamless and does not affect other projects
- No cross-project data or model leakage

---

## Testing Checklist
- [ ] New projects/namespaces can be created
- [ ] Data is isolated to each project
- [ ] Models are isolated to each project
- [ ] Switching context works as expected
- [ ] No cross-project leakage occurs

---

## Feedback & Improvements
- Report multi-project issues via GitHub Issues or project chat
- Suggest improvements to this journey doc via pull request
