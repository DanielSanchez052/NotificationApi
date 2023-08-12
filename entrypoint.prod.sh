# python manage.py flush --no-input
# python manage.py migrate

python manage.py collectstatic --noinput
python manage.py migrate --noinpu
gunicorn --config gunicorn-cfg.py NotificationApi.wsgi

# exec "$@"