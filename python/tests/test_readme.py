from pathlib import Path


def get_repo_root() -> Path:
    # python/tests/test_readme.py -> parents[2] is "python", parents[3] is repo root
    return Path(__file__).resolve().parents[3]


def test_readme_exists_and_sections():
    repo_root = get_repo_root()
    readme = repo_root / "README.md"
    assert readme.exists(), "README.md should exist at repository root"
    text = readme.read_text(encoding="utf-8")

    required_headings = [
        "# Gorgonaut",
        "## Ontology Alignment",
        "## API Specification",
        "## Repository Layout",
        "## Prerequisites",
        "## Quickstart",
        "## JavaScript",
        "## Python",
        "## Docker Compose",
        "## Contributing",
        "## License",
    ]
    for heading in required_headings:
        assert heading in text, f"Missing heading: {heading}"


def test_readme_links_exist_on_disk():
    repo_root = get_repo_root()
    expected_paths = [
        "docs/architecture/ontology-overview.md",
        "specs/ontology/gorgonaut-mindtools.ttl",
        "specs/ontology/gorgonaut-mindtools-shacl.ttl",
        "specs/ontology/data/examples.ttl",
        "specs/api/openapi.yaml",
        "js/apps/web/src/main.tsx",
    ]
    for rel in expected_paths:
        path = repo_root / rel
        assert path.exists(), f"Linked path should exist: {rel}"


def test_readme_commands_and_snippets_present():
    repo_root = get_repo_root()
    readme = repo_root / "README.md"
    text = readme.read_text(encoding="utf-8")

    # Makefile targets and python module runs
    expected_snippets = [
        "make spec.ontology.validate",
        "make spec.api.validate",
        "make web.dev",
        "uv run -m gorgonaut.tools.validate_shacl",
        "uv run -m gorgonaut.tools.validate_openapi",
        'import { hello } from "@gorgonaut/lib";',
    ]
    for snippet in expected_snippets:
        assert snippet in text, f"Expected snippet missing: {snippet}"


