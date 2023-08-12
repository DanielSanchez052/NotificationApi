# python manage.py flush --no-input
# python manage.py migrate

gunicorn --config gunicorn-cfg.py NotificationApi.wsgi
