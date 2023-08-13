import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.hackathon.settings")
app = Celery("hackathon")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
