from NotificationApi.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda f: [
                       s.strip() for s in f.split(',')])

# CSRF config
# CSRF_TRUSTED_ORIGINS = ["http://localhost:85", "http://127.0.0.1:85"]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# celery and redis
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


# CORS Config
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:85"
]
