from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


@dataclass(frozen=True)
class AppConfig:
    app_env: str
    log_level: str
    openapi_spec_path: Path

    @staticmethod
    def from_env() -> "AppConfig":
        # Load from .env if present (local dev/tests only)
        load_dotenv(override=False)
        app_env = os.getenv("APP_ENV", "development")
        log_level = os.getenv("LOG_LEVEL", "INFO")
        openapi_spec_path = Path(os.getenv("OPENAPI_SPEC_PATH", "specs/api/openapi.yaml")).resolve()
        return AppConfig(
            app_env=app_env,
            log_level=log_level,
            openapi_spec_path=openapi_spec_path,
        )


def fetch_secret_from_1password(
    item: str, field: str, vault: Optional[str] = None
) -> Optional[str]:
    """
    Fetch a secret value using 1Password CLI (`op`).
    Returns None if op is not available or the fetch fails.
    """
    import shutil
    import subprocess

    if shutil.which("op") is None:
        return None
    cmd = ["op", "item", "get", item, f"--field={field}"]
    if vault:
        cmd.extend(["--vault", vault])
    try:
        value = subprocess.check_output(cmd, text=True).strip()
        return value or None
    except Exception:
        return None
