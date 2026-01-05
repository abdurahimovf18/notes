from src.application.data_transfer_objects.note_dtos import NoteDeleteDTO, NoteIDDTO
from src.application.unit_of_work import UnitOfWork
from src.application.use_cases.use_case import UseCase


class NoteDeleteUseCase(UseCase[NoteDeleteDTO, NoteIDDTO]):
    
    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow

    async def execute(self, data: NoteDeleteDTO) -> NoteIDDTO:
        async with self._uow as uow:
            await uow.notes.delete(data.id)
            await uow.commit()

        return NoteIDDTO(id=data.id)
