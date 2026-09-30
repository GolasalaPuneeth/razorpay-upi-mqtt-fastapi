from sqlmodel import SQLModel, Field, create_engine, Session, select

# Database connection
DATABASE_URL = "postgresql+psycopg2://postgres:Admin123@localhost:5432/my_costume_database"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

# Model
class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    age: int

# Create table
SQLModel.metadata.create_all(engine)

# Insert record
with Session(engine) as session:
    student = Student(
        name="Puneeth",
        email="puneeth@example.com",
        age=27
    )

    session.add(student)
    session.commit()
    session.refresh(student)

    print("Inserted:", student)

# Fetch records
with Session(engine) as session:
    statement = select(Student)
    students = session.exec(statement).all()

    for student in students:
        print(student)