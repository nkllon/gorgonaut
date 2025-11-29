# Implementation Plan

- [x] 1. Standardize Docker Compose services for CI determinism
  - Define services: `python-validate`, `js-package` (and optional `web-build`) with pinned base images, system deps (graphviz), workspace mounts, working directories, and non-root users.
  - Provide `docker-compose.yml` targets that run `make ci` sub-steps with correct exit codes and artifact paths (`./artifacts/**`).
  - _Requirements: 2, 3_

- [x] 2. Makefile contracts as single source of truth
  - Ensure `make ci` calls: `py.install`, `py.lint`, `py.type`, `py.test`, `spec.ontology.validate`, `spec.api.validate`, `js.install`, `js.lint`, `js.test` with strict error propagation.
  - Add artifact output flags (e.g., `pytest --junitxml`, linter reports) and write to `./artifacts/`.
  - _Requirements: 1, 3_

- [x] 3. GitHub Actions workflows delegating to Make (P)
  - Create `.github/workflows/ci.yaml` with PR triggers; jobs invoke `make ci` and upload `./artifacts/**`.
  - Configure caching (npm, uv) and matrix where applicable; keep steps thin and avoid duplicating logic from Make.
  - _Requirements: 1, 3, 4_

- [ ] 4. Optional local Actions runner wrapper (P)
  - Provide a convenience script or docs to run workflows locally (e.g., with a local runner) that still defers to `make ci`.
  - Document known parity gaps and recommend Make as the contract when differences arise.
  - _Requirements: 1_

- [ ] 5. Documentation updates for contributor workflow
  - Add a concise section: prerequisites (Docker, uv, Node), how to run `make preflight`, `make ci`, and Compose variants; common failures/troubleshooting.
  - Link artifact locations and how CI publishes them; ensure commands are non-interactive and copy-pasteable.
  - _Requirements: 3, 4_

- [x] 6. Validation enhancements and artifacts (P)
  - Python: enable JUnit XML for pytest; ensure SHACL/OpenAPI validators return non-zero on failure and write logs to `./artifacts/specs/`.
  - JS: ensure eslint outputs machine-readable report in `./artifacts/js/`.
  - _Requirements: 2, 4_

- [ ] 7. Dev environment notes
  - Provide minimal devcontainer notes or section referencing containerized workflow; clarify supported versions and local vs container execution.
  - _Requirements: 4_


