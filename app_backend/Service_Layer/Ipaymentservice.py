from abc import ABC, abstractmethod
from sqlmodel.ext.asyncio.session import AsyncSession


class IPaymentHook(ABC):
    @abstractmethod
    async def process_payment(self, payment_data, session: AsyncSession):
        raise NotImplementedError