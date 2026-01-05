from src.application.data_transfer_objects.note_dtos import NoteCreateDTO, NoteIDDTO
from src.application.event_bus import EventBus
from src.application.ports.clock import Clock
from src.application.unit_of_work import UnitOfWork
from src.application.use_cases.use_case import UseCase
from src.domain.aggregates.note_aggregate import NoteAggregate


class NoteCreateUseCase(UseCase[NoteCreateDTO, NoteIDDTO]):

    def __init__(self, clock: Clock, uow: UnitOfWork, event_bus: EventBus) -> None:
        self._clock = clock
        self._uow = uow
        self._event_bus = event_bus

    async def execute(self, data: NoteCreateDTO) -> NoteIDDTO:
        now = self._clock.now()
        note = NoteAggregate.create(
            title=data.title, content=data.content, created_at=now
        )
        async with self._uow as uow:
            await uow.notes.add(note)
            await uow.commit()

        for event in note.pull_events():
            await self._event_bus.publish(event)

        return NoteIDDTO(id=note.id)
