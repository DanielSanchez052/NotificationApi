#!/bin/sh

exec python manage.py flush --no-input
exec python manage.py collectstatic --noinput
exec python manage.py migrate --noinput
exec gunicorn --config gunicorn-cfg.py NotificationApi.wsgi