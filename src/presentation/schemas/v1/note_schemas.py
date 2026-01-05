import uuid
from datetime import datetime

from pydantic import Field

from src.presentation.schemas.shared.base_schema import BaseSchema
from src.presentation.schemas.shared.pagination import PaginationRequestSchema


class NoteDetailSchema(BaseSchema):
    id: uuid.UUID
    version: int
    title: str
    content: str
    created_at: datetime


class NoteCreateSchema(BaseSchema):
    title: str
    content: str


class NoteListSchema(BaseSchema):
    id: uuid.UUID
    version: int
    title: str
    content: str
    created_at: datetime


class NoteUpdateSchema(BaseSchema):
    id: uuid.UUID
    version: int
    title: str | None
    content: str | None


class NoteDeleteSchema(BaseSchema):
    id: uuid.UUID


class NoteIDSchema(BaseSchema):
    id: uuid.UUID


class NotePaginationFilterSchema(PaginationRequestSchema):
    title_contains: str | None = Field(default=None)
