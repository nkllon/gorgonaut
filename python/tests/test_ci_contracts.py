import os


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def test_docker_compose_services_exist():
    compose_path = os.path.join(REPO_ROOT, "docker-compose.yml")
    assert os.path.exists(compose_path), "docker-compose.yml must exist at repo root"
    content = read(compose_path)
    assert "services:" in content
    assert "python-validate:" in content, "Service 'python-validate' must be defined"
    assert "js-package:" in content, "Service 'js-package' must be defined"


def test_makefile_ci_contracts_and_artifacts():
    makefile_path = os.path.join(REPO_ROOT, "Makefile")
    assert os.path.exists(makefile_path), "Makefile must exist at repo root"
    content = read(makefile_path)
    # ci must depend on these core targets
    for target in [
        "py.install",
        "py.lint",
        "py.type",
        "py.test",
        "spec.ontology.validate",
        "spec.api.validate",
        "js.install",
        "js.lint",
        "js.test",
    ]:
        assert f"ci: " in content and target in content, f"ci must include {target}"
    # py.test should emit junit xml into artifacts path
    assert "--junitxml artifacts/python/junit.xml" in content, (
        "pytest should write JUnit XML to artifacts/python/junit.xml"
    )
    # eslint should write a report to artifacts
    assert "eslint" in content and "--output-file artifacts/js/eslint.json" in content, (
        "eslint should write machine-readable report to artifacts/js/eslint.json"
    )


def test_github_actions_workflow_delegates_to_make_ci():
    workflow_path = os.path.join(REPO_ROOT, ".github", "workflows", "ci.yaml")
    assert os.path.exists(workflow_path), "GitHub Actions workflow .github/workflows/ci.yaml must exist"
    content = read(workflow_path)
    assert "on:" in content and "pull_request" in content
    assert "run: make ci" in content, "Workflow must delegate to `make ci`"


