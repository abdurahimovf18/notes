from src.application.data_transfer_objects.note_dtos import NoteDetailDTO, NoteIDDTO
from src.application.unit_of_work import UnitOfWork
from src.application.use_cases.use_case import UseCase


class NoteDetailUseCase(UseCase[NoteIDDTO, NoteDetailDTO]):

    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow

    async def execute(self, data: NoteIDDTO) -> NoteDetailDTO:
        async with self._uow as uow:
            note = await uow.notes.get(data.id)

        return NoteDetailDTO(
            id=note.id,
            version=note.version,
            title=note.title,
            content=note.content,
            created_at=note.created_at
        )
