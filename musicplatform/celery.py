
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplatform.settings')

celery = Celery('musicplatform')
celery.config_from_object('django.conf:settings', namespace='CELERY_CONF')
celery.autodiscover_tasks()
celery.conf.beat_schedule = settings.CELERY_CONF_BEAT_SCHEDULE