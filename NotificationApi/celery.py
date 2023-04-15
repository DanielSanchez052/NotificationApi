import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'NotificationApi.settings.local')

app = Celery('NotificationApi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def default_task(self):
    print(f'Request: {self.request}')
