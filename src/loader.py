import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.application.ports.clock import Clock
from src.application.unit_of_work import UnitOfWork
from src.config import settings
from src.core.application.event_bus import EventBus
from src.core.container import Container
from src.infrastructure.adapters.utc_clock import UTCClock
from src.infrastructure.rabbitmq_event_bus import RabbitMQEventBus
from src.infrastructure.sqlalchemy.setup import new_session
from src.infrastructure.unit_of_work import SQLAlchemyUnitOfWork
from src.presentation import api

logger = logging.getLogger(__name__)


class Loader:
    def __init__(self):
        self.container = Container()

    @asynccontextmanager
    async def lifespan(self, app: FastAPI) -> AsyncGenerator[None, None]:
        await self.startup()
        await self.setup_fastapi(app)
        yield
        await self.shutdown()

    async def startup(self):
        await self.setup_event_bus()
        await self.setup_unit_of_work()
        await self.setup_clock()

    async def shutdown(self):
        await self.cleanup_event_bus()

    async def setup_fastapi(self, app: FastAPI) -> None:
        app.dependency_overrides[api.dependency_injection.get_container] = (
            self.get_container
        ) 
        self.container.register_singleton(FastAPI, app)

    async def setup_event_bus(self) -> None:
        self.container.register_singleton(
            EventBus, 
            RabbitMQEventBus(
                self.container, 
                settings.RABBITMQ_USER, 
                settings.RABBITMQ_PASSWORD,
                settings.RABBITMQ_HOST,
                settings.RABBITMQ_PORT
            )
        )
        event_bus = await self.container.resolve(EventBus)
        await event_bus.start()

    async def cleanup_event_bus(self) -> None:
        event_bus = await self.container.resolve(EventBus)
        await event_bus.stop()

    async def setup_clock(self) -> None:
        self.container.register_singleton(Clock, UTCClock())

    async def setup_unit_of_work(self) -> None:
        self.container.register_sync_factory(
            UnitOfWork, 
            lambda: SQLAlchemyUnitOfWork(new_session)
        )

    async def get_container(self) -> Container:
        return self.container
    