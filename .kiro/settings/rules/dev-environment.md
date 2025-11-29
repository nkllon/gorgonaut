# Development Environment Rules (Dev Containers & Codespaces)

## Purpose
Define mandatory policies for local VS Code Dev Containers and GitHub Codespaces to ensure reproducible builds, predictable lifecycle, and cost-aware defaults.

## Tooling & Versions
- Node.js: 20.x via devcontainer feature
- Python: 3.12 via devcontainer feature
- Prefer `uv` for Python dependency management; fallback to `pip` in isolated venv
- System: install `graphviz` when validators are required

## Provisioning
- Post-create scripts must be non-interactive and idempotent:
  - `make install` (or equivalent) installs JS (npm) and Python (uv/pip) deps
  - Fail fast with clear logs and remediation guidance

## Ports & Debugging
- Forward ports: 5173 (Vite), 3000 (Web), 8000 (Python)
- Provide debug/launch configurations where applicable

## Lifecycle & Cost (Codespaces)
- Default machine size: 2-core unless a larger size is justified
- Encourage idle-stop and explicit stop/delete after sessions
- Document quotas and pricing link; warn about potential overages

## Secrets & Security
- Use platform secret stores only; never commit `.env` or credentials
- Least privilege; avoid root-only mutations where feasible
- Pin feature versions and document update cadence

## EARS Examples
1. The Dev Environment shall provision Node 20 and Python 3.12 via features.
2. When post-create runs, the Dev Environment shall install JS and Python dependencies without prompts.
3. If a required secret is missing, the Dev Environment shall block the dependent task and output setup instructions.
4. While running in Codespaces, the Dev Environment shall prefer a 2-core machine size unless overridden by the developer.


