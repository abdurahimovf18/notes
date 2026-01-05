from fastapi import APIRouter

from . import system, v1

router = APIRouter()
router.include_router(system.router)
router.include_router(v1.router)
