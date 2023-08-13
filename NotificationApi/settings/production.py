import os
from NotificationApi.settings.base import * # NOQA
from decouple import config
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', default=False))
print("OS: " + os.environ.get('DEBUG', default=False))
print("DEBUG: " + DEBUG)

ALLOWED_HOSTS = [s.strip() for s in os.environ.get('ALLOWED_HOSTS', default="").split(',')]

# CSRF config
CSRF_TRUSTED_ORIGINS = ["http://localhost:85", "http://127.0.0.1:85"]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

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

# celery and redis
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


# CORS Config
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:85"
]


# NOTIFICATION QUEUE
NOTIFICATIONS_QUEUE_BATCH = 20
