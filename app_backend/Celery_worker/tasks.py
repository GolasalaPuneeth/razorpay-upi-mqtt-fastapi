from .config import celery_app
from Database_Layer import tranx_device_logs, TransactionLogs

@celery_app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    max_retries=5
)
def test_task(self,data,sync_session):
    tranx_device_logs(TransactionLogs(trx_metadata=data),sync_session)
    return True