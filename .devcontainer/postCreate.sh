#!/usr/bin/env bash
set -euo pipefail

echo "[postCreate] Updating apt and installing system packages (graphviz)"
if command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update -y
  sudo apt-get install -y --no-install-recommends graphviz
else
  echo "[postCreate] apt-get not available; skipping system graphviz install"
fi

echo "[postCreate] Installing repo dependencies via Makefile"
if command -v make >/dev/null 2>&1; then
  make install
else
  echo "[postCreate] make not found; running fallback installers"
  # JS workspaces
  if [ -d "js" ]; then
    (cd js && (npm ci || npm i))
  fi
  # Python via uv if available; otherwise pip
  if command -v uv >/dev/null 2>&1 || [ -x "$HOME/.local/bin/uv" ]; then
    UV_BIN="$(command -v uv 2>/dev/null || echo "$HOME/.local/bin/uv")"
    (cd python && "$UV_BIN" sync --extra dev)
  else
    echo "[postCreate] uv not found; using pip fallback"
    python3 -m pip install --upgrade pip
    (cd python && python3 -m pip install -e .[dev])
  fi
fi

echo "[postCreate] Done."


