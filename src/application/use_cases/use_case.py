from typing import Protocol

from src.application.data_transfer_objects.data_transfer_object import DataTransferObject


class UseCase[I: DataTransferObject, O: DataTransferObject](Protocol):
    async def execute(self, data: I) -> O: ...
