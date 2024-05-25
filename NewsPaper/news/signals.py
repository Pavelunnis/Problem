from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from .models import PostCategory
from django.dispatch import receiver



@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, **kwargs):
    if not kwargs["action"] == 'post_add':
        emails = User.objects.filter(
            subscriptions__category__in=instance.postCategory.all()
        ).values_list('email', flat=True)

        subject = f'Новая запись в категории {instance.postCategory}'

        text_content = (
            f'Новость: {instance.heading}\n'
            f'Текст: {instance.textPost}\n\n'
            f'Ссылка на новость: http://127.0.0.1:8000{instance.get_absolute_url()}'
        )
        html_content = (
            f'Новость: {instance.heading}<br>'
            f'Текст: {instance.textPost}<br><br>'
            f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
            f'Ссылка на новость</a>'
        )
        for email in emails:
            msg = EmailMultiAlternatives(subject, text_content, None, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()