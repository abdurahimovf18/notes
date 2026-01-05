from src.application.queries.note.filters import NoteFilter
from src.application.queries.pagination import PaginationQuery, PaginationResult
from src.application.repositories.repository import Repository
from src.domain.aggregates.note_aggregate import NoteAggregate


class NoteRepository(Repository[NoteAggregate]):
    
    async def filter_list(
            self, 
            filters: NoteFilter,
            pagination: PaginationQuery
        ) -> PaginationResult[NoteAggregate]:
        ...
        