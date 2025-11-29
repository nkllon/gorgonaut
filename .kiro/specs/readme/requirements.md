# Requirements — Feature: readme

## Goal
Create a top-level `README.md` that:
- Aligns terminology and framing with the project ontology in `specs/ontology/`
- Provides clear implementation and usage guidance for the JS workspaces and Python tooling
- Documents validation flows for OpenAPI and SHACL
- Explains repo layout and common developer workflows (Makefile, Docker Compose)

## Scope
- Repository-level `README.md` only
- Cross-reference to existing docs under `docs/` and `specs/`
- Include minimal code snippets (JS lib usage) and terminal commands (Make targets)
- Audience: developers and contributors (first-time and returning)

## Non-Goals
- Full API user manual (the API is minimal; we only link to `specs/api/openapi.yaml`)
- Ontology deep-dive (link to `docs/architecture/ontology-overview.md` and the Turtle files)
- Publishing/CI setup changes

## Constraints
- Keep consistent with current structure and scripts:
  - Make targets: `install`, `py.*`, `js.*`, `spec.*`, `web.dev`, `ci`, `ci-docker`
  - Docker Compose services: `python-validate`, `python-export`, `js-package`, `web-build`
  - JS workspace via `js/package.json` (npm workspaces; Node 20, npm 10)
  - Python via `uv` and `python/pyproject.toml`
- Use English (spec.json.language = "en")

## Acceptance Criteria
- README includes:
  - High-level overview consistent with ontology classes and purpose
  - Repo layout summary (JS apps/packages, Python tooling, specs, docs)
  - Quickstart with Makefile and uv/npm prerequisites
  - Validation commands for SHACL and OpenAPI (Makefile and Python module forms)
  - Web app dev instructions and JS lib usage example
  - Docker Compose CI-like flows
  - Links to ontology overview and OpenAPI spec
- All referenced paths and commands are accurate and executable given current repo


