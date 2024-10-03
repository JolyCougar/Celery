import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_django.settings')

app = Celery('celery_django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-spam-every-5-minute': {
        'task': 'send_mail.tasks.send_beat_email',
        'schedule': crontab(minute='*/5'),
    }
}