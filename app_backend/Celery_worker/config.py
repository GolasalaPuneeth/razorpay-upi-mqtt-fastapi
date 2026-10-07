from dotenv import load_dotenv
from celery import Celery
import os


load_dotenv()

REDIS_URL : str  = os.getenv("REDIS_URL")

celery_app : Celery = Celery(
    "payment_worker",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["Celery_worker.tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
)