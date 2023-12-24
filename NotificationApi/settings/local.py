import os
from NotificationApi.settings.base import * # NOQA
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', default="1")

ALLOWED_HOSTS = [s.strip() for s in os.environ.get('ALLOWED_HOSTS', default="").split(',')]

# CSRF config
CSRF_TRUSTED_ORIGINS = ["http://localhost:85", "http://127.0.0.1:85", "http://localhost:8000", "http://127.0.0.1:8000", "http://localhost:5005", "http://127.0.0.1:5005"]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(os.path.join(BASE_DIR.parent, "dbNotifications.sqlite3")), # NOQA
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
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = config("EMAIL_HOST", default='smtp.gmail.com')
# EMAIL_HOST_USER = config("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = 587

NOTIFICATIONS_QUEUE_BATCH = 20

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': "[{server_time}]%(levelname)s %(message)s"
        },
    },
    'handlers':
    {
        'log_to_stdout':
        {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'main': {
            'handlers': ['log_to_stdout'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

CRONTAB_COMMAND_PREFIX = (
    'STAGE=production'
)

# cron-jobs
CRONJOBS = [
    ('* * * * *', 'django.core.management.call_command', ['run_queued_notifications'], {}, '>> /cron/django_cron.log2>&1')
]
