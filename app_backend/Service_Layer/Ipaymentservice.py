from abc import ABC, abstractmethod
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import Session


class IPaymentHook(ABC):
    @abstractmethod
    async def process_payment(self, payment_data, session: AsyncSession, sync_session:Session):
        raise NotImplementedError("Subclasses must implement this method")