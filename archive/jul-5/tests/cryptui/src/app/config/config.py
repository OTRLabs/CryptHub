import os
import json
from pathlib import Path
from dataclasses import dataclass
from functools import lru_cache
from typing import Any
from litestar import Litestar
from litestar.config import Config

def get_settings() -> dict[str, Any]:
    CRYPT_UI_HOST=os.environ.get("CRYPT_UI_HOST", "localhost")
    CRYPT_UI_PORT=int(os.environ.get("CRYPT_UI_PORT", 8000))
    CRYPT_UI_BASE_ROUTE=os.environ.get("CRYPT_UI_BASE_ROUTE", "/")
    CRYPT_UI_API_ROUTE=CRYPT_UI_BASE_ROUTE+"api"
    CRYPT_UI_STATIC_ROUTE=CRYPT_UI_BASE_ROUTE+"static"
    
    