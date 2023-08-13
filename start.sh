#!/bin/sh

# exec python manage.py flush --no-input
# exec python manage.py migrate --noinput

python manage.py collectstatic --noinput

exec gunicorn --config gunicorn-cfg.py NotificationApi.wsgi