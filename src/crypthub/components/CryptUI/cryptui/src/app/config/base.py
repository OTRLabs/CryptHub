from __future__ import annotations

import binascii
import json
import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final


if TYPE_CHECKING:
    from litestar.data_extractors import RequestExtractorField, ResponseExtractorField

DEFAULT_MODULE_NAME = "app"


TRUE_VALUES = {"True", "true", "1", "yes", "Y", "T"}


@dataclass
class SurrealDBConfig:
    """SurrealDB Configuration

    Args:
        host (str): The hostname of the SurrealDB server.
        port (int): The port of the SurrealDB server.
        namespace (str): The namespace of the SurrealDB database.
        db (str): The database name of the SurrealDB database.
        username (str): The username of the SurrealDB server.
        password (str): The password of the SurrealDB server.
    """

    host: str = field(
        default_factory=lambda: os.environ.get("SURREAL_DB_HOST", "localhost") in TRUE_VALUES,
    )
    port: int = field(
        default_factory=lambda: int(os.environ.get("SURREAL_DB_PORT", 8000)),
    )
    namespace: str = field(
        default_factory=lambda: os.environ.get("SURREAL_DB_NAMESPACE", "default"),
    )
    
    db: str = field(
        default_factory=lambda: os.environ.get("SURREAL_DB_NAME", "default"),
    )
    username: str = field(
        default_factory=lambda: os.environ.get("SURREAL_DB_USERNAME", "root"),
    )
    password: str = field(
        default_factory=lambda: os.environ.get("SURREAL_DB_PASSWORD", "root"),
    )