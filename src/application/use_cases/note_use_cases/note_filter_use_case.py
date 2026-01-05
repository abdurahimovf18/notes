from src.application.data_transfer_objects.note_dtos import NoteListDTO, NotePaginationFilterDTO
from src.application.data_transfer_objects.shared import PaginationResultDTO
from src.application.queries.note.filters import NoteFilter
from src.application.queries.pagination import PaginationQuery
from src.application.unit_of_work import UnitOfWork
from src.application.use_cases.use_case import UseCase


class NoteFilterUseCase(UseCase[NotePaginationFilterDTO, PaginationResultDTO[NoteListDTO]]):
    
    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow

    async def execute(self, data: NotePaginationFilterDTO) -> PaginationResultDTO[NoteListDTO]:
        async with self._uow as uow:
            result = await uow.notes.filter_list(
                filters=NoteFilter(title_contains=data.title_contains),
                pagination=PaginationQuery(page=data.page, items_per_page=data.items_per_page)
            )

        dto_items = [
            NoteListDTO(
                id=note.id,
                version=note.version,
                title=note.title,
                content=note.content,
                created_at=note.created_at
            ) 
            for note in result.items
        ]

        return PaginationResultDTO(
            items=dto_items,
            page=result.page,
            last_page=result.last_page,
            items_per_page=result.items_per_page
        )
            