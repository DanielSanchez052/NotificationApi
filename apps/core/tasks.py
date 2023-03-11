from celery import shared_task
from celery.utils.log import get_task_logger

from django.conf import settings
from django.core.mail import EmailMultiAlternatives


@shared_task(name='send email')
def send_async_email(subject: str, emails: list, text_msg: str, html_msg: str, mimetype: str = "text/html"):
    try:
        email = EmailMultiAlternatives(
            # title:
            subject,
            # body text:
            text_msg,
            # from:
            settings.EMAIL_HOST_USER,
            # to:
            emails
        )
        email.attach_alternative(html_msg, mimetype=mimetype)
        email.send()
        return f'Email Sended to {emails}'

    except Exception as e:
        return str(e)
