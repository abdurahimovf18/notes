from collections.abc import Awaitable, Callable
from typing import Protocol


class Container(Protocol):
    def register_sync_factory[T](
            self, 
            interface: type[T], 
            factory: Callable[[], T]
        ) -> None: ...

    def register_async_factory[T](
            self, 
            interface: type[T], 
            factory: Callable[[], Awaitable[T]]
        ) -> None: ...

    def register_singleton[T](self, interface: type[T], singleton: T) -> None: ...

    async def resolve[T](self, interface: type[T]) -> T: ...
    
    def _check_not_registered(self, interface: type[object]) -> None: ...
