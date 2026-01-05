import uuid
from datetime import datetime
from typing import Self

from src.domain.aggregates.aggregate import Aggregate
from src.domain.entities.note_entity import NoteEntity


class NoteAggregate(NoteEntity, Aggregate):

    @classmethod
    def create(
            cls, 
            title: str, 
            content: str, 
            created_at: datetime
        ) -> Self:
        return cls(
            id=uuid.uuid4(),
            version=1,
            title=title,
            content=content,
            created_at=created_at
        )

