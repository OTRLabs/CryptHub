import os
from typing import cast, Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, Session, sessionmaker

from advanced_alchemy.base import UUIDBase
from advanced_alchemy.filters import LimitOffset
from advanced_alchemy.repository import SQLAlchemySyncRepository
from advanced_alchemy.utils.fixtures import open_fixture

def get_database_connection() -> str:
    pass