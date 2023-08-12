from NotificationApi.settings.base import * # NOQA
from decouple import config
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda f: [s.strip() for s in f.split(',')])

# CSRF config
CSRF_TRUSTED_ORIGINS = ["http://localhost:85", "http://127.0.0.1:85"]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config("SQL_ENGINE"),
        'NAME': config("SQL_DATABASE"),
        'HOST': config("SQL_HOST"),
        'USER': config("SQL_USER"),
        'PASSWORD': config("SQL_PASSWORD"),
        'PORT': config("SQL_PORT")
    }
}

# celery and redis
CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND")
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
