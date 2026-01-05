import uuid
from dataclasses import dataclass, field
from datetime import datetime

from src.application.data_transfer_objects.shared.data_transfer_object import DataTransferObject
from src.application.data_transfer_objects.shared.pagination_dtos import BasePaginationDTO


@dataclass(slots=True, frozen=True)
class NoteDetailDTO(DataTransferObject):
    id: uuid.UUID
    version: int
    title: str
    content: str
    created_at: datetime


@dataclass(slots=True, frozen=True)
class NoteCreateDTO(DataTransferObject):
    title: str
    content: str


@dataclass(slots=True, frozen=True)
class NoteListDTO(DataTransferObject):
    id: uuid.UUID
    version: int
    title: str
    content: str
    created_at: datetime


@dataclass(slots=True, frozen=True)
class NoteUpdateDTO(DataTransferObject):
    id: uuid.UUID
    version: int
    title: str | None
    content: str | None


@dataclass(slots=True, frozen=True)
class NoteDeleteDTO(DataTransferObject):
    id: uuid.UUID


@dataclass(slots=True, frozen=True)
class NoteIDDTO(DataTransferObject):
    id: uuid.UUID


@dataclass(slots=True, frozen=True)
class NotePaginationFilterDTO(BasePaginationDTO):
    title_contains: str | None = field(default=None)
