#!/bin/sh


python manage.py flush --no-input
python manage.py collectstatic --noinput
python manage.py migrate --noinput

gunicorn --config gunicorn-cfg.py NotificationApi.wsgi

# exec "$@"