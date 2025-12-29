from datetime import UTC
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parent.parent.parent


class Env(BaseSettings):
    # System settings
    DEBUG: Literal["true", "false"]
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    
    # Database settings
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    # Rabbitmq settings
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int

    # Redis settings
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str
    REDIS_DB: int

    model_config = SettingsConfigDict(
        env_file=ROOT / ".env"
    )


env = Env()  # type: ignore

# System settings
DEBUG: bool = env.DEBUG == "true"
TIMEZONE = UTC

# Logging settings
LOG_LEVEL = env.LOG_LEVEL
LOG_FILE_PATH = ROOT / "resources" / "app.log"
LOG_FORMAT = "[%(asctime)s] %(levelname)s in %(name)s:%(lineno)d — %(message)s"

# Postgresql settings
POSTGRES_USER = env.POSTGRES_USER 
POSTGRES_PASSWORD = env.POSTGRES_PASSWORD
POSTGRES_HOST = env.POSTGRES_HOST
POSTGRES_PORT = env.POSTGRES_PORT
POSTGRES_DB = env.POSTGRES_DB 

# Redis settings
RABBITMQ_USER = env.RABBITMQ_USER 
RABBITMQ_PASSWORD = env.RABBITMQ_PASSWORD
RABBITMQ_HOST = env.RABBITMQ_HOST
RABBITMQ_PORT = env.RABBITMQ_PORT

# Redis settings
REDIS_HOST = env.REDIS_HOST
REDIS_PORT = env.REDIS_PORT
REDIS_PASSWORD = env.REDIS_PASSWORD
REDIS_DB = env.REDIS_DB
