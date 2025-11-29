# Research & Design Decisions

---
**Purpose**: Capture discovery findings, architectural investigations, and rationale that inform the technical design.
---

## Summary
- **Feature**: github-ci-local-workflow-validation
- **Discovery Scope**: Complex Integration
- **Key Findings**:
  - The repo already defines canonical `make ci` and `ci-docker` targets integrating Python/JS validators and spec checks; these are the basis for local parity.
  - Containerized execution via Docker Compose is referenced but requires standardized service definitions to ensure deterministic environments and parity with CI.
  - When GitHub Actions workflows are added, a local runner (e.g., `act`) can mirror job steps; where parity gaps exist, the Makefile remains the single source of truth.

## Research Log

### Local CI Parity Strategy
- **Context**: Prevent PR check failures by ensuring contributors can run the identical checks locally.
- **Sources Consulted**: Internal Makefile, monorepo structure, steering docs.
- **Findings**:
  - `make ci` covers py lint/type/test, SHACL, OpenAPI, JS install/lint/test.
  - `make ci-docker` invokes Compose services (`python-validate`, `js-package`, etc.), implying planned container boundaries.
  - No `.github/workflows` currently; the design should define how Actions invoke the same Make targets to guarantee parity.
- **Implications**: Make targets become contract; Actions and local runners must call them, not duplicate logic.

### Deterministic Tooling
- **Context**: Eliminating environment drift.
- **Findings**:
  - Python uses `uv` to pin and run tools (ruff, black, mypy, pytest, validators).
  - JS uses `npm ci` with lockfile; lint/tests run under workspace.
  - Some system deps (e.g., `graphviz`) should be provided via container images to avoid host variance.
- **Implications**: Compose services must include system packages and cache behavior; CI and local envs call the same containers.

### Local Actions Runner
- **Context**: Running GitHub workflows locally where applicable.
- **Findings**:
  - A local runner can provide convenience but may not fully support all Actions features.
  - Using Make targets behind Actions jobs limits divergence and simplifies parity.
- **Implications**: Prefer “Actions → Make” invocation; local runner optional, Make remains the contract.

## Architecture Pattern Evaluation
| Option | Description | Strengths | Risks / Limitations | Notes |
|--------|-------------|-----------|---------------------|-------|
| Makefile as single source of truth | Actions and local use the same Make targets | Minimal duplication, strong parity | Requires discipline to avoid drift | Aligns with current repo |
| Direct Actions scripting | Steps written only in workflows | Easy to add | Diverges from local dev, harder to reproduce | Not recommended |
| Local runner primary (`act`) | Run workflows locally | Familiar UX | Parity gaps for edge cases | Use as convenience wrapper |

## Design Decisions

### Decision: Makefile-first parity with containerized services
- **Context**: Avoid drift between local and CI.
- **Alternatives Considered**: Direct Actions scripting; ad-hoc scripts.
- **Selected Approach**: All CI checks are implemented as Make targets. Actions jobs and local commands call Make, optionally inside Docker Compose services.
- **Rationale**: Ensures a single definitive set of checks with deterministic environments.
- **Trade-offs**: Requires maintaining Make/Compose definitions; minor learning curve.
- **Follow-up**: Provide minimal Compose services and document usage.

## Risks & Mitigations
- Tool/version drift — Pin via `uv` and `npm ci`; bake images with system deps.
- Incomplete local parity — Keep Actions jobs thin; call Make targets.
- Developer environment variance — Provide Compose path and devcontainer guidance.

## References
- Internal steering docs: `.kiro/steering/{product,tech,structure}.md`
- Repo Makefile contracts: `make ci`, `make ci-docker`


