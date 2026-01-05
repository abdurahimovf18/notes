from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.config import settings

DATABASE_URL = (
    f"postgresql+psycopg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)

engine = create_async_engine(
    url=DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=10,
    max_overflow=40,
    pool_timeout=30,
    pool_recycle=1800,
)

new_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

metadata = MetaData()
