#!/bin/sh
printenv > /etc/environment

service cron start

python manage.py crontab remove
python manage.py crontab add
python manage.py crontab show


exec "$@"