from datetime import datetime
from uuid import UUID

from src.domain.entities.domain_entity import DomainEntity
from src.domain.exceptions.note_exceptions import (
    NoteContentTooLongError,
    NoteTitleTooLongError,
    NoteTitleTooShortError,
)


class NoteEntity(DomainEntity):
    
    def __init__(
            self, 
            id: UUID, 
            version: int,
            title: str,
            content: str,
            created_at: datetime
        ) -> None:
        super().__init__(id, version)

        self._check_title(title)
        self._check_content(content)

        self._title = title
        self._content = content
        self._created_at = created_at

    @property
    def title(self) -> str:
        return self._title
    
    @property
    def content(self) -> str:
        return self._content
    
    @property
    def created_at(self) -> datetime:
        return self._created_at
    
    def change_title(self, value: str) -> None:
        self._check_title(value)
        self._title = value
    
    def change_content(self, value: str) -> None:
        self._check_content(value)
        self._content = value

    @staticmethod
    def _check_title(value: str) -> None:
        max_letters_length = 255
        min_letters_length = 3

        if len(value) > max_letters_length:
            raise NoteTitleTooLongError(
                f"Note title must contain at most {max_letters_length} letters."
            )
        
        if len(value) < min_letters_length:
            raise NoteTitleTooShortError(
                f"Note title must contain at least {min_letters_length} letters."
            )
    
    @staticmethod
    def _check_content(value: str) -> None:
        max_letters_length = 1500

        if len(value) > max_letters_length:
            raise NoteContentTooLongError(
                f"Note content must contain at most {max_letters_length} letters."
            )
    