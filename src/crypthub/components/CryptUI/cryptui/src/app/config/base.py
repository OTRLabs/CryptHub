
import binascii
import json
import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from litestar.utils.module_loader import module_to_os_path

from typing import TYPE_CHECKING, Any, Final
from surrealdb import SurrealDB

if TYPE_CHECKING:
    from litestar.data_extractors import RequestExtractorField, ResponseExtractorField

DEFAULT_MODULE_NAME = "app"
BASE_DIR: Final[Path] = module_to_os_path(DEFAULT_MODULE_NAME)

TRUE_VALUES = {"True", "true", "1", "yes", "Y", "T"}


@dataclass
class SurrealDatabaseConfig:
    host: str
    port: int
    namespace: str
    user: str
    password: str
    
    