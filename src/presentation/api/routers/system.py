from typing import Literal

from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def ping() -> Literal["pong"]:
    return "pong"
