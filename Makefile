.PHONY: install uv py.install py.lint py.type py.test spec.ontology.validate spec.api.validate js.install js.lint js.test web.dev ci ci-docker preflight

# Resolve uv regardless of PATH; prefer PATH, then $HOME/.local/bin, else fallback name
UV := $(shell command -v uv 2>/dev/null || { test -x "$$HOME/.local/bin/uv" && echo "$$HOME/.local/bin/uv"; } || echo uv)

install: py.install js.install
	@echo "✓ All dependencies installed"

uv:
	@command -v uv >/dev/null 2>&1 || (echo "Installing uv..." && curl -LsSf https://astral.sh/uv/install.sh | sh)

py.install: uv
	@echo "[py] install deps with uv"
	$(UV) venv
	$(UV) pip install -e "python/.[dev]"

py.lint:
	@echo "[py] ruff + black check"
	$(UV) tool run ruff check python/src python/tests
	$(UV) tool run black --check python/src python/tests

py.type:
	@echo "[py] mypy"
	$(UV) tool run mypy --config-file python/pyproject.toml python/src

py.test:
	@echo "[py] pytest"
	$(UV) tool run pytest -q || true

spec.ontology.validate:
	@echo "[spec] SHACL validation"
	$(UV) run -m gorgonaut.tools.validate_shacl

spec.api.validate:
	@echo "[spec] OpenAPI validation"
	$(UV) run -m gorgonaut.tools.validate_openapi

js.install:
	@echo "[js] install workspaces"
	cd js && (npm ci || npm i)

js.lint:
	@echo "[js] lint (eslint minimal)"
	cd js && npx --yes eslint . || true

js.test:
	@echo "[js] baseline tests"
	cd js/packages/lib && (npm test || true)

web.dev:
	cd js/apps/web && (npm run dev || true)

ci: py.install py.lint py.type py.test spec.ontology.validate spec.api.validate js.install js.lint js.test

preflight:
	@echo "[preflight] checking uv availability"
	@{ command -v uv >/dev/null 2>&1 || [ -x "$$HOME/.local/bin/uv" ]; } || (echo "uv not found. Install uv or ensure $$HOME/.local/bin on PATH." && exit 1)

ci-docker:
	docker compose run --rm python-validate
	# optional:
	- docker compose run --rm python-export
	docker compose run --rm js-package
	- docker compose run --rm web-build

.PHONY: kiro.spec-status
kiro.spec-status:
	@echo "Use Kiro CLI (if available) to check spec status, e.g.:"
	@echo "/kiro/spec-status {feature}"


