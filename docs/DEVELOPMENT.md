# Development Workflow

## Container-First Development
All development, testing, and automation must be run inside Docker containers. No code should be run directly on the host machine.

## Container Checks and Automation
Before starting any workflow step (development, testing, build, etc.), you must ensure all required containers are running. Use the provided script:

```bash
bash scripts/container_check_and_build.sh
```
- This script checks for all required services (see `REQUIRED_SERVICES` in `scripts/container_check_and_build.sh`).
- If any are missing, it (re)builds and starts them using `docker-compose`.

### Adding New Services
- When the project grows and new containers/services are added, update the `REQUIRED_SERVICES` array in `scripts/container_check_and_build.sh` to include them.
- Document new containers in `/docs/README.md` and update `docker/docker-compose.yml` accordingly.

## Container Discovery & Troubleshooting
- To see all running containers:
  ```bash
  docker compose ps
  ```
- If a container is missing or not running, use the check-and-build script above.
- All onboarding, troubleshooting, and automation must reference the current state of containers.

## CI/CD Pipeline
As of this writing, **there is no dedicated CI/CD pipeline present in the project**. When CI/CD is added, it must:
- Run all jobs inside containers (never on the host)
- Use the same container check/build logic as local development
- Document pipeline configuration in `/docs/README.md` and/or `/docs/DEVELOPMENT.md`

---

_Last updated: 2025-04-26T20:01:49-06:00_
