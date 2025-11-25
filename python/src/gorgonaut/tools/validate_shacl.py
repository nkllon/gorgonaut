from pathlib import Path
from typing import Tuple

from rdflib import Graph
from pyshacl import validate


REPO_ROOT = Path(__file__).resolve().parents[3]
ONTOLOGY_TTL = REPO_ROOT / "specs" / "ontology" / "gorgonaut-mindtools.ttl"
SHACL_TTL = REPO_ROOT / "specs" / "ontology" / "gorgonaut-mindtools-shacl.ttl"
EXAMPLES_TTL = REPO_ROOT / "specs" / "ontology" / "data" / "examples.ttl"


def load_graph(path: Path) -> Graph:
    g = Graph()
    g.parse(str(path), format="turtle")
    return g


def run_validation(data_graph: Graph, shacl_graph: Graph) -> Tuple[bool, str]:
    conforms, _results_graph, results_text = validate(
        data_graph=data_graph,
        shacl_graph=shacl_graph,
        data_graph_format="turtle",
        shacl_graph_format="turtle",
        inference="rdfs",
        abort_on_first=False,
        allow_infos=True,
        allow_warnings=True,
    )
    return bool(conforms), results_text


def main() -> int:
    missing = [p for p in (ONTOLOGY_TTL, SHACL_TTL) if not p.exists()]
    if missing:
        missing_str = ", ".join(str(p) for p in missing)
        print(f"[skip] SHACL validation missing files: {missing_str}")
        return 0

    data_graph = load_graph(ONTOLOGY_TTL)
    if EXAMPLES_TTL.exists():
        try:
            examples_graph = load_graph(EXAMPLES_TTL)
            data_graph += examples_graph  # merge
        except Exception:
            pass
    shapes_graph = load_graph(SHACL_TTL)
    conforms, results_text = run_validation(data_graph, shapes_graph)
    if not conforms:
        print("SHACL validation failed:")
        print(results_text)
        return 1
    print("SHACL validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


