#!/bin/sh

# exec python manage.py flush --no-input
# exec python manage.py migrate --noinput

python manage.py collectstatic --no-input

exec gunicorn --config gunicorn-cfg.py NotificationApi.wsgi