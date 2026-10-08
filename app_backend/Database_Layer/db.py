from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine, Session
from sqlmodel.ext.asyncio.session import AsyncSession
from dotenv import load_dotenv
import os
load_dotenv()

DATABASE_URL=os.getenv('DATABASE_URL')
SYNC_DATABASE_URL = os.getenv('SYNC_DATABASE_URL')
async_engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True)
engine = create_engine(SYNC_DATABASE_URL, echo=True)

def get_sync_session():
    with Session(engine) as session:
        yield session

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI Dependency Injection for AsyncSession."""
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session