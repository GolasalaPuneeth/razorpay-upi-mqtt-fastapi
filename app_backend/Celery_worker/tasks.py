from .config import celery_app
from Database_Layer import tranx_device_logs, TransactionLogs,engine
from sqlmodel import Session
from App_Utils import MQTTTool

mqtttool:MQTTTool = MQTTTool()

@celery_app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    max_retries=5
)

# Checked Celery working..
def test_task(self,data):
    with Session(engine) as sync_session:
        tranx_device_logs(TransactionLogs(trx_metadata=data),sync_session)
    mqtttool.publish_message("test","hello")
    return True