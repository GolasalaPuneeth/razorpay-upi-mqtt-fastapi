from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

# Note driver change: asyncpg instead of psycopg2
DATABASE_URL = (
    "postgresql+asyncpg://postgres:Admin123@localhost:5432/my_costume_database"
)

async_engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True)


async def init_db() -> None:
    """Creates database tables asynchronously."""
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI Dependency Injection for AsyncSession."""
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session