#!/bin/sh

python manage.py collectstatic --no-input

exec gunicorn --config gunicorn-cfg.py NotificationApi.wsgi 