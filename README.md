# Gorgonaut — Mind Tools Ontology and Expert-System Framing

Gorgonaut models the Mind Tools corpus as an ontology and frames an expert system that is context-aware and stakeholder-sensitive. The ontology captures key entities like MetaSkill, Tool, ProblemType, Outcome, and Stakeholder, and organizes expert-system layers (ContextEngine, ToolSynthesisEngine, DecisionActionLayer, CapabilityBuildingLayer) for selecting and composing tools into actionable workflows.

## Ontology Alignment
- Overview: see `docs/architecture/ontology-overview.md`
- Ontology (Turtle): `specs/ontology/gorgonaut-mindtools.ttl`
- SHACL shapes: `specs/ontology/gorgonaut-mindtools-shacl.ttl`
- Example data: `specs/ontology/data/examples.ttl`

Validate ontology conformance with SHACL:

```bash
make spec.ontology.validate
# or directly via Python tooling
cd python && uv run -m gorgonaut.tools.validate_shacl
```

## API Specification
- OpenAPI: `specs/api/openapi.yaml`

Validate OpenAPI:

```bash
make spec.api.validate
# or directly via Python tooling
cd python && uv run -m gorgonaut.tools.validate_openapi
```

## Repository Layout
- `js/` — JavaScript monorepo (npm workspaces)
  - `apps/web/` — Vite React app
  - `packages/lib/` — Shared TypeScript library (`@gorgonaut/lib`)
- `python/` — Python package (`gorgonaut`) and validation tools
- `specs/` — Ontology and API specifications
- `docs/` — Architecture notes and reports
- `Makefile` — Common developer workflows
- `docker-compose.yml` — CI-like flows in containers

## Prerequisites
- Node 20 and npm 10 (see `js/package.json`)
- uv (Python package/dependency manager)

Install uv if needed:

```bash
make uv
```

## Quickstart
Install all dependencies for Python and JS:

```bash
make install
```

Run validations:

```bash
make spec.ontology.validate
make spec.api.validate
```

Start the web app (dev):

```bash
make web.dev
# or directly:
cd js/apps/web && npm run dev
```

## JavaScript
Install JS workspaces:

```bash
make js.install
```

Library build and tests:

```bash
cd js/packages/lib
npm run typecheck
npm run build
npm test
```

Use `@gorgonaut/lib`:

```ts
import { hello } from "@gorgonaut/lib";

console.log(hello("World")); // "Hello, World!"
```

Web app (Vite + React):
- App entry: `js/apps/web/src/main.tsx`
- Dev: `npm run dev`
- Build: `npm run build`

## Python (uv-managed)
Sync and run validators:

```bash
cd python
uv sync --extra dev
uv run -m gorgonaut.tools.validate_shacl
uv run -m gorgonaut.tools.validate_openapi
```

Lint, type-check, test:

```bash
make py.lint
make py.type
make py.test
```

## Docker Compose (CI-like)
Run validation and builds in containers:

```bash
docker compose run --rm python-validate
docker compose run --rm js-package
docker compose run --rm web-build
```

## Contributing
PRs welcome. Before submitting:

```bash
make install
make ci
```

## License
MIT (see `python/pyproject.toml`); a root `LICENSE` file may be added in the future.


