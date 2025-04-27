# WORKSPACE RULES for Semantic System

## MCP Server Sequential-Thinking Integration

- All next steps, planning, and task breakdowns MUST be managed using the MCP server's sequential-thinking tool.
- If the MCP server or sequential-thinking plan is missing, agents must automatically set it up and ensure it is running.
- All automation, agent, and AI behavior must defer to the MCP sequential-thinking plan as the operational source of truth.
- If a master project plan document (such as /docs/planning/SEMANTIC_SYSTEM_MASTER_CHECKLIST.md) exists, use the MCP server's sequential-thinking plan to break down the plan into granular, prioritized tasks and sub-tasks, strictly following the master plan. Do NOT inject new ideas; strictly follow the master plan.
- As tasks are completed, update both the MCP server plan and the markdown checklist to keep both in sync.
- If there are multiple steps left in the plan, do not ask the user for new ideas. Continue working on the planned tasks unless the user explicitly interrupts the plan.

## Containerization and Testing

- All development, testing, and automation must run inside Docker containers.
- No host virtualenv activation is required or supported for project automation.
- Install all project dependencies (including dev/test tools) in the Docker image.

## Documentation

- Document all decisions, design choices, and implementation details.
- Place new design docs in /docs/design-docs/.
- Add new planning/status docs to /docs/planning/.
- Add onboarding or high-level intros to /docs/onboarding/.
- Place guides and how-tos in /docs/guides/.
- Always update /docs/README.md when adding new documentation.
- Cross-link relevant docs for context and onboarding.

## Testing Requirements

- Unit tests are required for all new components and functions.
- Integration tests are required for API endpoints and service interactions.
- End-to-end tests are required for user-facing features.
- Test before proceeding to the next phase or deployment.
