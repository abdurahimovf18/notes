import uuid
from typing import Protocol

from src.domain.aggregates.aggregate import Aggregate


class Repository[T: Aggregate](Protocol):

    async def edit(self, aggregate: T) -> None: 
        """Updates AggregateRoot"""
        ...

    async def add(self, aggregate: T) -> None:
        """Creates new AggregateRoot in the storage"""
        ...

    async def delete(self, id: uuid.UUID) -> None: 
        """Deletes an AggregateRoot by ID"""
        ...

    async def get(self, id: uuid.UUID) -> T:
        """Executes self.get_by_id inside"""
        ...
        