"""
WSGI config for NotificationApi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os
from distutils.util import strtobool

from django.core.wsgi import get_wsgi_application


debug = strtobool(os.environ.get('DEBUG', default=False))
settings_module = 'NotificationApi.settings.production' if not debug else 'NotificationApi.settings.local'

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "NotificationApi.settings.production")

application = get_wsgi_application()
