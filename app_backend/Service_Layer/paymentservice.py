from .Ipaymentservice import IPaymentHook
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import Session
from Database_Layer import create_trx_log, TransactionLogs
from App_Utils import MQTTTool

mqtt_tool:MQTTTool = MQTTTool()

class PaymentHook(IPaymentHook):

    async def process_payment(self, payment_data,session:AsyncSession,sync_session:Session):
        print(f"payment_data_service_layer -----------> {payment_data}")
        await create_trx_log(tranxlogs=TransactionLogs(trx_metadata=str(payment_data)),session=session)
        # need to add filtering data
        # this is a basic structure if needed engage celery workers
        mqtt_tool.publish_message("test","test_data")
        return {"status": "success", "message": "Payment processed successfully."}