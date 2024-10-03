from django.core.mail import send_mail
from celery_django.celery import app
from celery import shared_task
from .service import send
from .models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку',
            'Мы будем присылать вам много сообщений в течении 5 минут',
            'danero95@yandex.ru',
            [contact.email],
            fail_silently=False,
        )


@app.task
def my_task(a, b):
    c = a + b
    return c


@app.task(bind=True, default_retry_delay=5 * 60)
def my_task_retry(self, x, y):
    try:
        return x + y
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@shared_task()
def my_sh_task(msg):
    return msg + "!!!"
