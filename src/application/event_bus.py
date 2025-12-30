from collections.abc import Awaitable, Callable
from typing import Protocol

from src.application.ports.container import Container
from src.domain.events.domain_event import DomainEvent


class EventBus(Protocol):
    async def publish(self, event: DomainEvent) -> None: ...

    def subscribe[T: DomainEvent](
            self, 
            event: type[T], 
            handler: Callable[[T, Container], Awaitable[None]]
        ) -> None: ...

    async def start(self): ...

    async def stop(self): ...
    