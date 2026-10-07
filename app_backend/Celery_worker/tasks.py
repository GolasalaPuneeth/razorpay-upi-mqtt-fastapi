from .config import celery_app

@celery_app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    max_retries=5
)
def test_task(self,data):
    print("working")
    return True