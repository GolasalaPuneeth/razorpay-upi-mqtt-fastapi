from sqlmodel import Field, SQLModel


class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    age: int

class transaction_logs(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    metadata: str

class device_logs(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    device_id: str
    trx_status: str

class device_settings(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    device_id: str
    settings: str