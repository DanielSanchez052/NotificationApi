from celery import shared_task
from celery.utils.log import get_task_logger

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
