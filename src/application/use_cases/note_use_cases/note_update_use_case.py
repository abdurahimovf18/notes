from src.application.data_transfer_objects.note_dtos import NoteIDDTO, NoteUpdateDTO
from src.application.event_bus import EventBus
from src.application.exceptions.repository_exceptions import VersionMismatchError
from src.application.unit_of_work import UnitOfWork
from src.application.use_cases.use_case import UseCase


class NoteUpdateUseCase(UseCase[NoteUpdateDTO, NoteIDDTO]):
    
    def __init__(self, uow: UnitOfWork, event_bus: EventBus) -> None:
        self._uow = uow
        self._event_bus = event_bus

    async def execute(self, data: NoteUpdateDTO) -> NoteIDDTO:
        async with self._uow as uow:
            note = await uow.notes.get(id=data.id)

            if note.version != data.version:
                raise VersionMismatchError(
                    "Cannot update note due to a concurrent modification."
                )
            note.change_title(data.title or note.title)
            note.change_content(data.content or note.content)
            await uow.notes.edit(note)
            await uow.commit()

        for event in note.pull_events():
            await self._event_bus.publish(event)

        return NoteIDDTO(id=data.id)
