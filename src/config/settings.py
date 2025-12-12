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
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str

    # Broker settings
    BROKER_USER: str
    BROKER_PASSWORD: str
    BROKER_HOST: str
    BROKER_PORT: int

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

# Database settings
DATABASE_USER = env.DATABASE_USER 
DATABASE_PASSWORD = env.DATABASE_PASSWORD
DATABASE_HOST = env.DATABASE_HOST
DATABASE_PORT = env.DATABASE_PORT
DATABASE_NAME = env.DATABASE_NAME 

# RabbitMQ settings
BROKER_USER = env.BROKER_USER 
BROKER_PASSWORD = env.BROKER_PASSWORD
BROKER_HOST = env.BROKER_HOST
BROKER_PORT = env.BROKER_PORT

AMQP_URL = (
    f"amqp://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}"
)
