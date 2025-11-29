# Design — Feature: readme

## Structure
1. Project title and one-paragraph overview aligned to ontology:
   - Mention core classes (MetaSkill, Tool, ProblemType, Outcome, Stakeholder, ExpertSystem layers)
   - State purpose: expert-system framing over Mind Tools ontology
2. Ontology alignment section:
   - Link to `docs/architecture/ontology-overview.md`
   - Link to Turtle files and SHACL
3. Repository layout:
   - Summarize `js/` (apps/web, packages/lib), `python/`, `specs/`, `docs/`
4. Quickstart:
   - Prereqs: Node 20 + npm 10, uv
   - `make install`, validation, and dev commands
5. Validation flows:
   - SHACL and OpenAPI via Makefile and Python modules
6. JavaScript:
   - Workspaces install
   - Web app dev instructions
   - Library usage example (`@gorgonaut/lib` with `hello`)
7. Python:
   - uv sync and running validators
8. Docker Compose:
   - CI-style invocations for validation, packaging, and build
9. API spec:
   - Link to `specs/api/openapi.yaml`
10. Contributing / License (concise; leverage existing metadata)

## Style
- Concise, action-oriented sections with code fences only for commands or short examples
- Prefer relative paths and Make targets to minimize drift
- Avoid deep ontology exposition; link to sources


