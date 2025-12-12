from sqlalchemy.orm import DeclarativeBase

from src.infrastructure.sqlalchemy.setup import metadata


class BaseModel(DeclarativeBase):
    metadata = metadata
    