from dataclasses import dataclass

from src.application.data_transfer_objects.shared.data_transfer_object import DataTransferObject


@dataclass(slots=True, frozen=True)
class PaginationResultDTO[T: DataTransferObject](DataTransferObject):
    items: list[T]
    page: int
    last_page: int
    items_per_page: int


@dataclass(slots=True, frozen=True)
class BasePaginationDTO(DataTransferObject):
    page: int
    items_per_page: int
