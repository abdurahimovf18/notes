import math
import uuid

import sqlalchemy as sa
from sqlalchemy.exc import DataError, IntegrityError

from src.application.exceptions.repository_exceptions import (
    AggregateAlreadyExistsError,
    AggregateNotFoundError,
    PaginationOutOfRangeError,
)
from src.application.queries.note.filters import NoteFilter
from src.application.queries.pagination import PaginationQuery, PaginationResult
from src.application.repositories.note_repository import NoteRepository
from src.domain.aggregates.note_aggregate import NoteAggregate
from src.infrastructure.repositories.sqlalchemy.sqlalchemy_repository import SqlAlchemyRepository
from src.infrastructure.sqlalchemy.models import NoteModel


class SqlAlchemyNoteRepository(SqlAlchemyRepository, NoteRepository):
    
    async def filter_list(
            self, filters: NoteFilter, pagination: PaginationQuery
        ) -> PaginationResult[NoteAggregate]:
        base_query = sa.select(NoteModel)

        if filters.title_contains is not None:
            pattern = f"%{filters.title_contains}%"
            base_query = base_query.where(NoteModel.title.ilike(pattern))

        limit = pagination.items_per_page
        offset = pagination.page * pagination.items_per_page

        try:
            items_query = base_query.limit(limit).offset(offset)
            result = await self._session.execute(items_query)
            items = result.scalars().all()
            print(items)

            count_query = sa.select(sa.func.count()).select_from(base_query.subquery())
            count_result = await self._session.execute(count_query)
            total_count = count_result.scalar_one()
        except DataError as exc:
            raise PaginationOutOfRangeError(
                "Attempt to run pagination with unprocessable pagination fields."
            ) from exc

        pagination_items = [
            NoteAggregate(
                id=note_model.id,
                version=note_model.version,
                title=note_model.title,
                content=note_model.content,
                created_at=note_model.created_at
            )
            for note_model in items
        ]
        return PaginationResult(
            items=pagination_items,
            page=pagination.page,
            last_page=max(math.ceil(total_count / limit) - 1, 0),
            items_per_page=limit
        )

    async def edit(self, aggregate: NoteAggregate) -> None:
        aggregate.increment_version()

        try:
            await self._session.execute(
                sa.update(NoteModel)
                .filter_by(id=aggregate.id)
                .values(
                    id=aggregate.id,
                    version=aggregate.version,
                    title=aggregate.title,
                    content=aggregate.content,
                    created_at=aggregate.created_at
                )
            )
        except IntegrityError as exc:
            raise AggregateAlreadyExistsError(
                "Note with this title already exists."
            ) from exc
        
    async def add(self, aggregate: NoteAggregate) -> None:
        try:
            await self._session.execute(
                sa.insert(NoteModel)
                .values(
                    id=aggregate.id,
                    version=aggregate.version,
                    title=aggregate.title,
                    content=aggregate.content,
                    created_at=aggregate.created_at
                )
            )
        except IntegrityError as exc:
            raise AggregateAlreadyExistsError(
                "Note with this title already exists."
            ) from exc

    async def delete(self, id: uuid.UUID) -> None: 
        await self._session.execute(sa.delete(NoteModel).filter_by(id=id))

    async def get(self, id: uuid.UUID) -> NoteAggregate:
        result = await self._session.execute(sa.select(NoteModel).filter_by(id=id))
        model = result.scalar_one_or_none()
        if model is None:
            raise AggregateNotFoundError("Note with this id could not be found.")
        
        return NoteAggregate(
            id=model.id,
            version=model.version,
            title=model.title,
            content=model.content,
            created_at=model.created_at
        )
        