# Requirements Document

## Introduction
This specification ensures all GitHub CI workflows are reliably validated locally, using containers and deterministic tooling, so PR commit checks never fail due to untested or environment-specific differences. The scope covers GitHub Actions parity, containerized local execution, deterministic toolchains, preflight developer workflows, and clear documentation.

## Requirements

### Requirement 1: Local parity for GitHub Actions workflows
**Objective:** As a contributor, I want to run the full PR CI suite locally, so that I can catch failures before pushing.

#### Acceptance Criteria
1. When a developer runs a single documented command, the local runner shall execute the same jobs/steps as PR CI (workflow parity).
2. If a GitHub workflow uses services (e.g., matrix, Docker services), the local run shall provision equivalent containers and networks.
3. While running locally, the system shall produce exit codes identical to CI pass/fail for gating.
4. Where job conditionals exist (on: pull_request, push), the local runner shall support selecting CI context (e.g., PR vs push).
5. The local run shall generate human-readable logs and summarize failures matching CI job names.

### Requirement 2: Containerized and deterministic local CI tooling
**Objective:** As a maintainer, I want containerized toolchains, so that CI results are reproducible across machines.

#### Acceptance Criteria
1. When executing locally, Python tasks shall run with pinned tool versions (uv/venv), including ruff, black, mypy, pytest, openapi validator, and SHACL validator.
2. When executing locally, JavaScript tasks shall run with pinned Node/npm and lockfile integrity (npm ci), including ESLint, type-check, build, and tests.
3. The system shall provide Docker/Docker Compose definitions or prebuilt images to encapsulate environment dependencies (e.g., graphviz).
4. The system shall avoid host-global state; caches and artifacts shall be stored in workspace-relative locations.
5. The system shall expose a non-interactive mode suitable for automation and CI parity.

### Requirement 3: PR check reliability and developer preflight
**Objective:** As a reviewer, I want PR checks to be consistently green when preflight succeeds locally, so that review time is not wasted.

#### Acceptance Criteria
1. When a developer runs the documented preflight command, all PR-required checks shall pass locally before push.
2. If any required check fails locally, the command shall exit non-zero and show actionable failure details.
3. The repository shall define a canonical preflight target (e.g., `make ci` or `npm run ci`), referenced in documentation and CI.
4. The preflight shall validate OpenAPI (`specs/api/openapi.yaml`) and SHACL/ontology (`specs/ontology/*`) as part of the default checks.
5. The preflight shall be runnable inside a dev container and on host with Docker installed.

### Requirement 4: Documentation, discoverability, and artifacts
**Objective:** As a new contributor, I want clear docs and artifacts, so that I can quickly run CI locally and interpret results.

#### Acceptance Criteria
1. The repository shall include a concise guide section explaining local CI execution, prerequisites, and common failure modes.
2. The local runner shall emit logs/artifacts (e.g., junit, coverage, lints) in known paths for inspection and CI upload.
3. The documentation shall specify supported OS/tool versions and how to obtain them (devcontainer, Docker, or platform package managers).
4. Commands shall be copy-pasteable and non-interactive by default.
5. The documentation shall link troubleshooting for Docker/network constraints and platform differences.

