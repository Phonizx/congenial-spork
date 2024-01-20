import time

from celery import Celery

from app.settings import settings

celery = Celery(__name__)
celery.conf.broker_url = settings.CELERY_BROKER_URL
celery.conf.result_backend = settings.CELERY_RESULT_BACKEND


@celery.task(name="create_task")
def create_task(a, b, c):
    time.sleep(a)
    print(b + c)
