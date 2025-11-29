# Implementation Plan

## Task List

- [ ] 1. Create unified Dev Container configuration (local + Codespaces)
  - Add `.devcontainer/devcontainer.json` with features: Node 20, Python 3.12, common-utils; pin feature versions.
  - Configure `customizations.vscode.extensions` (Python, ESLint, Prettier, Dev Containers).
  - Define `forwardPorts` and `portsAttributes` for 5173, 3000, 8000.
  - _Requirements: 1, 2, 3, 8, 9_

- [ ] 1.1 Define postCreate/update provisioning (P)
  - JS: run `(npm ci || npm i)` in `js/` workspaces; ensure non-interactive.
  - Python: prefer `uv pip install -e ./python`; fallback to `python -m pip install -e ./python` and required deps.
  - Install OS-level `graphviz` when validators are used.
  - _Requirements: 2, 3, 4_

- [ ] 2. Add optional `.devcontainer/Dockerfile` if features insufficient
  - Base on `mcr.microsoft.com/devcontainers/base` (or Debian/Ubuntu) and install required packages.
  - Keep image minimal and pinned; avoid embedding secrets.
  - _Requirements: 2, 9_

- [ ] 3. Expose workspace tasks and scripts
  - JS library: build, typecheck, test in `js/packages/lib`.
  - Web app: build/preview in `js/apps/web`.
  - Python: SHACL and OpenAPI validators.
  - Provide VS Code tasks or `make` targets for one-command flows.
  - _Requirements: 3, 4_

- [ ] 4. Codespaces defaults and lifecycle controls
  - Document default machine size (2-core) and how to scale up.
  - Document idle timeout/retention settings and stop/delete guidance.
  - Link to pricing calculator and quota information.
  - _Requirements: 5, 6_

- [ ] 5. Secrets and environment configuration
  - Document using platform secret stores (Codespaces secrets, local env/devcontainer features).
  - Validate presence of required secrets in tasks; fail with remediation hints.
  - _Requirements: 7, 9_

- [ ] 6. Debugging and ports
  - Provide launch configurations for Python and Vite where applicable.
  - Ensure ports are forwarded and visibility is correct in Codespaces.
  - _Requirements: 8_

- [ ] 7. Validation and smoke tests (P)
  - Verify container builds on Apple Silicon and x86_64.
  - Run `npm ci && build && test` (JS) and Python validators successfully.
  - Confirm port forwarding and access to dev servers.
  - _Requirements: 1, 2, 3, 4, 8_

- [ ] 8. Security hardening
  - Avoid running as root where feasible; scope privileges.
  - Pin feature versions and document update cadence.
  - _Requirements: 9_


