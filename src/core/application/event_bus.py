from abc import ABC, abstractmethod
from collections.abc import Awaitable, Callable

from src.core.container import Container
from src.core.domain.domain_event import DomainEvent


class EventBus(ABC):
    
    @abstractmethod
    async def publish(self, event: DomainEvent) -> None: ...

    @abstractmethod
    def subscribe[T: DomainEvent](
            self, 
            event: type[T], 
            handler: Callable[[T, Container], Awaitable[None]]
        ) -> None: ...

    @abstractmethod
    async def start(self): ...

    @abstractmethod
    async def stop(self): ...
    
    def __repr__(self) -> str:
        return f"<{type(self).__name__}>"
    