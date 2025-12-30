import logging
import logging.config

from fastapi import FastAPI

from src.config import settings
from src.loader import Loader

__all__ = [
    "app",
]

logging.config.dictConfig(settings.LOGGING_DICT_CONFIG)

app = FastAPI(lifespan=Loader().lifespan)
