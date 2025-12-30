import uuid
from typing import Protocol

from src.domain.aggregates.aggregate import Aggregate


class Repository[T: Aggregate](Protocol):
    
    async def get_by_id(self, id: uuid.UUID) -> T | None: 
        """Returns an AggregateRoot by ID if exists, otherwise returns None"""

    async def edit(self, aggregate_root: T) -> None: 
        """Updates AggregateRoot"""

    async def add(self, aggregate_root: T) -> None:
        """Creates new AggregateRoot in the storage"""

    async def delete(self, id: uuid.UUID) -> None: 
        """Deletes an AggregateRoot by ID"""

    async def exists(self, id: uuid.UUID) -> bool:
        """Checks if the AggregateRoot exists"""
        ...

    async def get(self, id: uuid.UUID) -> T | None:
        """Executes self.get_by_id inside"""
        return await self.get_by_id(id)

    def __repr__(self) -> str:
        return f"<{type(self).__name__}>"
    