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
