from .models import TransactionLogs
from sqlmodel import select,Session
from sqlmodel.ext.asyncio.session import AsyncSession


async def create_trx_log(tranxlogs: TransactionLogs, session: AsyncSession) -> TransactionLogs:
    """Inserts a new student into the database."""
    session.add(tranxlogs)
    await session.commit()
    await session.refresh(tranxlogs)
    return tranxlogs

def tranx_device_logs(data: TransactionLogs,sync_session:Session):
    sync_session.add(data)
    sync_session.commit()





# async def get_all_students(session: AsyncSession) -> list[Student]:
#     """Fetches all students from the database."""
#     statement = select(Student)
#     result = await session.exec(statement)
#     return list(result.all())