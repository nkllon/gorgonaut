from pathlib import Path
from openapi_spec_validator import validate_spec
from openapi_spec_validator.readers import read_from_filename

REPO_ROOT = Path(__file__).resolve().parents[3]
OPENAPI_PATH = REPO_ROOT / "specs" / "api" / "openapi.yaml"


def main() -> int:
    if not OPENAPI_PATH.exists():
        print(f"[skip] OpenAPI spec not found: {OPENAPI_PATH}")
        return 0
    spec_dict, _ = read_from_filename(str(OPENAPI_PATH))
    validate_spec(spec_dict)
    print("OpenAPI validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


