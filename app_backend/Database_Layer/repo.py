from .models import TransactionLogs
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


async def create_trx_log(tranxlogs: TransactionLogs, session: AsyncSession) -> TransactionLogs:
    """Inserts a new student into the database."""
    session.add(tranxlogs)
    await session.commit()
    await session.refresh(tranxlogs)
    return tranxlogs




# async def get_all_students(session: AsyncSession) -> list[Student]:
#     """Fetches all students from the database."""
#     statement = select(Student)
#     result = await session.exec(statement)
#     return list(result.all())