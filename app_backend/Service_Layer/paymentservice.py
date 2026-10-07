from .Ipaymentservice import IPaymentHook
from sqlmodel.ext.asyncio.session import AsyncSession
from Database_Layer import create_trx_log, TransactionLogs

class PaymentHook(IPaymentHook):

    async def process_payment(self, payment_data,session:AsyncSession):
        print(f"payment_data_service_layer -----------> {payment_data}")
        await create_trx_log(tranxlogs=TransactionLogs(trx_metadata=str(payment_data)),session=session)
        

        return {"status": "success", "message": "Payment processed successfully."}