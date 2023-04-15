from NotificationApi.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda f: [
                       s.strip() for s in f.split(',')])

# celery and redis
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# CSRF config
# CSRF_TRUSTED_ORIGINS = ["http://localhost:85", "http://127.0.0.1:85"]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(os.path.join(BASE_DIR, "dbNotifications.sqlite3")),
    }
    # "default": {
    #     "ENGINE": "mssql",
    #     "HOST": "DESKTOP-I412VA9",
    #     "NAME": "dbNotifications",
    #     "USER": "daniel.sanchez",
    #     "PASSWORD": "Admin123*",
    #     "PORT": ""
    # }
}

# CORS Config
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:85"
]


# send Email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = config("EMAIL_HOST", default='smtp.gmail.com')
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
