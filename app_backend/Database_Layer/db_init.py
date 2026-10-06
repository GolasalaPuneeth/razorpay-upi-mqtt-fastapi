from .db import async_engine
from .models import SQLModel


async def init_db() -> None:
    """Creates database tables asynchronously."""
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)