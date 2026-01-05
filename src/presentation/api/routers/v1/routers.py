from fastapi import APIRouter, Body, HTTPException, Query, status

from src.application.data_transfer_objects.note_dtos import (
    NoteCreateDTO,
    NoteDeleteDTO,
    NoteIDDTO,
    NotePaginationFilterDTO,
    NoteUpdateDTO,
)
from src.application.event_bus import EventBus
from src.application.ports.clock import Clock
from src.application.unit_of_work import UnitOfWork
from src.application.use_cases.note_use_cases.note_create_use_case import NoteCreateUseCase
from src.application.use_cases.note_use_cases.note_delete_use_case import NoteDeleteUseCase
from src.application.use_cases.note_use_cases.note_detail_use_case import NoteDetailUseCase
from src.application.use_cases.note_use_cases.note_filter_use_case import NoteFilterUseCase
from src.application.use_cases.note_use_cases.note_update_use_case import NoteUpdateUseCase
from src.presentation.api.dependency_injection import Container
from src.presentation.schemas.shared.pagination import PageResponseSchema
from src.presentation.schemas.v1.note_schemas import (
    NoteCreateSchema,
    NoteDeleteSchema,
    NoteDetailSchema,
    NoteIDSchema,
    NoteListSchema,
    NotePaginationFilterSchema,
    NoteUpdateSchema,
)
from src.shared.exceptions.conflict_error import ConflictError
from src.shared.exceptions.forbidden_error import ForbiddenError
from src.shared.exceptions.invalid_data_error import InvalidDataError
from src.shared.exceptions.validation_error import ValidationError

router = APIRouter(prefix="/v1")


@router.get("/notes", status_code=status.HTTP_200_OK)
async def get_notes(
        container: Container, data: NotePaginationFilterSchema = Query()  # noqa
    ) -> PageResponseSchema[NoteListSchema]:
    use_case = NoteFilterUseCase(uow=await container.resolve(UnitOfWork))
    try:
        result = await use_case.execute(
            NotePaginationFilterDTO(
                page=data.page,
                items_per_page=data.items_per_page,
                title_contains=data.title_contains
            )
        )
    except InvalidDataError as exc:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, exc.message) from exc

    return PageResponseSchema(
        items=[NoteListSchema.model_validate(item.to_dict()) for item in result.items],
        page=result.page,
        items_per_page=result.items_per_page,
        last_page=result.last_page
    )


@router.post("/notes", status_code=status.HTTP_201_CREATED)
async def create_note(
        container: Container, data: NoteCreateSchema = Body()  # noqa
    ) -> NoteIDSchema:
    
    use_case = NoteCreateUseCase(
        clock=await container.resolve(Clock),
        uow=await container.resolve(UnitOfWork),
        event_bus=await container.resolve(EventBus)
    )

    try:
        result = await use_case.execute(NoteCreateDTO(title=data.title, content=data.content))
    except ValidationError as exc:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, exc.message) from exc
    except ConflictError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, exc.message) from exc

    return NoteIDSchema.model_validate(result.to_dict())


@router.get("/notes/{note_id}", status_code=status.HTTP_200_OK)
async def get_note_detail(
        container: Container, data: NoteIDSchema = Query()  # noqa
    ) -> NoteDetailSchema:

    use_case = NoteDetailUseCase(uow=await container.resolve(UnitOfWork))
    result = await use_case.execute(NoteIDDTO(id=data.id))
    return NoteDetailSchema.model_validate(result.to_dict())


@router.delete("/notes", status_code=status.HTTP_200_OK)
async def delete_note(
        container: Container, data: NoteDeleteSchema = Body()  # noqa
    ) -> NoteIDSchema:
    use_case = NoteDeleteUseCase(uow=await container.resolve(UnitOfWork))
    result = await use_case.execute(NoteDeleteDTO(id=data.id))
    return NoteIDSchema.model_validate(result.to_dict())


@router.patch("/notes/{note_id}")
async def update_note(
        container: Container, data: NoteUpdateSchema = Body()  # noqa
    ) -> NoteIDSchema:
    
    use_case = NoteUpdateUseCase(
        uow=await container.resolve(UnitOfWork),
        event_bus=await container.resolve(EventBus)
    )
    try:
        result = await use_case.execute(
            NoteUpdateDTO(id=data.id, version=data.version, title=data.title, content=data.content)
        )
    except ForbiddenError as exc:
        raise HTTPException(status.HTTP_403_FORBIDDEN, exc.message) from exc
    except ValidationError as exc:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, exc.message) from exc
    except ConflictError as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, exc.message) from exc
    
    return NoteIDSchema.model_validate(result.to_dict())

