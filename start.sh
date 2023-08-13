#!/bin/sh

# exec python manage.py flush --no-input
# exec python manage.py migrate --noinput

exec python manage.py collectstatic

exec gunicorn --config gunicorn-cfg.py NotificationApi.wsgi