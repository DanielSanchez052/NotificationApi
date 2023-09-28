import os
from NotificationApi.settings.base import * # NOQA
from decouple import config
from distutils.util import strtobool
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = strtobool(os.environ.get('DEBUG', default="0"))

ALLOWED_HOSTS = [s.strip() for s in os.environ.get('ALLOWED_HOSTS', default="localhost").split(',')]

# CSRF config
CSRF_TRUSTED_ORIGINS = [s.strip() for s in os.environ.get('CSRF_TRUSTED_ORIGINS').split(',')]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if "DATABASE_URL" in os.environ :
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get("SQL_ENGINE", default="django.db.backends.mysql"),
            'NAME': os.environ.get("SQL_DATABASE"),
            'HOST': os.environ.get("SQL_HOST"),
            'USER': os.environ.get("SQL_USER"),
            'PASSWORD': os.environ.get("SQL_PASSWORD"),
            'PORT': os.environ.get("SQL_PORT")
        }
    }

# CORS Config
CORS_ALLOWED_ORIGINS = [s.strip() for s in os.environ.get('CORS_ALLOWED_ORIGINS').split(',')]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "POST",
    "PUT"]


# cron-jobs
CRONJOBS = [
    ('*/5 * * * *', 'django.core.management.call_command', ['run_queued_notifications'], {}, '>> /home/app/cron/notifications.log 2>&1')
]


# NOTIFICATION QUEUE
NOTIFICATIONS_QUEUE_BATCH = 20
