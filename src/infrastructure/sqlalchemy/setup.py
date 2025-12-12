from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.config import settings

# SqlAlchemy URL
# {db}+{driver}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}
DATABASE_URL = (
    f"postgresql+psycopg://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}"
    f"@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
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
