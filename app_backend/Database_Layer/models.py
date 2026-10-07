from sqlmodel import Field, SQLModel


class TransactionLogs(SQLModel, table=True):
    __tablename__ = "transaction_logs"

    id: int | None = Field(default=None, primary_key=True)
    trx_metadata: str

class DeviceLogs(SQLModel, table=True):
    __tablename__ = "device_logs"

    id: int | None = Field(default=None, primary_key=True)
    device_id: str
    trx_status: str
    trx_metadata: str
    
class DeviceSettings(SQLModel, table=True):
    __tablename__ = "device_settings"

    id: int | None = Field(default=None, primary_key=True)
    device_id: str
    settings: str