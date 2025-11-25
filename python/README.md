# Gorgonaut Python (uv-managed)

Install (locally with uv):
```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv pip install -e ".[dev]"
```

Run tests:
```
pytest -q
```

Validate OpenAPI:
```
python -m gorgonaut.tools.validate_openapi
```

Validate SHACL:
```
python -m gorgonaut.tools.validate_shacl
```


