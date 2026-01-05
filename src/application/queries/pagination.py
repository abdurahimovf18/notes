
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PaginationQuery:
    page: int
    items_per_page: int


@dataclass(frozen=True, slots=True)
class PaginationResult[T: object]:
    items: list[T]
    page: int
    last_page: int
    items_per_page: int
