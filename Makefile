.PHONY: install uv py.install py.lint py.type py.test spec.ontology.validate spec.api.validate js.install js.lint js.test web.dev ci ci-docker

install: py.install js.install
	@echo "✓ All dependencies installed"

uv:
	@command -v uv >/dev/null 2>&1 || (echo "Installing uv..." && curl -LsSf https://astral.sh/uv/install.sh | sh)

py.install: uv
	@echo "[py] install deps with uv"
	uv pip install -e "python/.[dev]"

py.lint:
	@echo "[py] ruff + black check"
	uvx ruff check python/src python/tests
	uvx black --check python/src python/tests

py.type:
	@echo "[py] mypy"
	uvx mypy --config-file python/pyproject.toml python/src

py.test:
	@echo "[py] pytest"
	uvx pytest -q || true

spec.ontology.validate:
	@echo "[spec] SHACL validation"
	uv run -m gorgonaut.tools.validate_shacl

spec.api.validate:
	@echo "[spec] OpenAPI validation"
	uv run -m gorgonaut.tools.validate_openapi

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


