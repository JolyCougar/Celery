from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на рассылку!',
        'Мы будем присылать ва много спама',
        'Danero95@yandex.ru',
        [user_email],
        fail_silently=False,
    )
