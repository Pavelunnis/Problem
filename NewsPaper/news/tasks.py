from celery import shared_task
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_mail_for_sub_once(sub_username, sub_useremail, html_content):
    print('Задача_одно_письмо - старт')
    msg = EmailMultiAlternatives(
        subject=f'Здравствуй, {sub_username}. Новая статья в вашем разделе!',
        from_email='SkillfactoryTest112@yandex.ru',
        to=[sub_useremail]
    )

    msg.attach_alternative(html_content, 'text/html')

    print()
    print(html_content)
    print()

    msg.send()
    print('Таска_одно_письмо - конец')


@shared_task
def send_mail_every_week(sub_username, sub_useremail, html_content):
    print('Задача_много_писем - старт')
    msg = EmailMultiAlternatives(
        subject=f'Здравствуй, {sub_username}, новые статьи за прошлую неделю в вашем разделе!',
        from_email='SkillfactoryTest112@yandex.ru',
        to=[sub_useremail]
    )

    msg.attach_alternative(html_content, 'text/html')
    print()

    print(html_content)

    msg.send()
    print('Задачи_много_писем - стоп')