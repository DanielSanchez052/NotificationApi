"""
WSGI config for NotificationApi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os
from decouple import config

from django.core.wsgi import get_wsgi_application

debug = config('DEBUG', default=False, cast=bool)
settings_module = 'NotificationApi.settings.production' if not debug else 'NotificationApi.settings.local'

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "NotificationApi.settings.production")

application = get_wsgi_application()
