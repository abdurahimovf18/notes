from src.presentation.schemas.shared.base_schema import BaseSchema


class PaginationRequestSchema(BaseSchema):
    page: int
    items_per_page: int


class PageResponseSchema[T: BaseSchema](BaseSchema):
    items: list[T]
    page: int
    items_per_page: int
    last_page: int
