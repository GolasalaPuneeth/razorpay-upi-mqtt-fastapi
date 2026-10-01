from models import Student
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


async def create_student(session: AsyncSession, student: Student) -> Student:
    """Inserts a new student into the database."""
    session.add(student)
    await session.commit()
    await session.refresh(student)
    return student


async def get_all_students(session: AsyncSession) -> list[Student]:
    """Fetches all students from the database."""
    statement = select(Student)
    result = await session.exec(statement)
    return list(result.all())