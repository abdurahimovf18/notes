import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.infrastructure.sqlalchemy.setup import metadata


class BaseModel(DeclarativeBase):
    metadata = metadata
    

class NoteModel(BaseModel):
    __tablename__ = "notes"

    id: Mapped[uuid.UUID] = mapped_column(sa.UUID(as_uuid=True), primary_key=True)
    version: Mapped[int]
    title: Mapped[str] = mapped_column(unique=True)
    content: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True))

    __table_args__ = (
        sa.Index("notes_title_index", "title"),
    )
