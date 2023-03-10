import json

from celery import shared_task, Task
from django.conf import settings
from django.utils.module_loading import import_string
from celery.utils.log import get_task_logger

from apps.notifications.models import Notification
from .strategy.context import Context

logger = get_task_logger(__name__)


class TaskLogs(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))
        return super().on_failure(exc, task_id, args, kwargs, einfo)

    def on_success(self, retval, task_id, args, kwargs):
        print('{0!r} Success: {1!r}'.format(task_id, retval))
        return super().on_success(retval, task_id, args, kwargs)


@shared_task(name="run_queued_notifications", base=TaskLogs)
def run_notifications():
    # execute notifications in pending
    notifications = Notification.objects.filter(
        notification_status=Notification.NotificationStatus.PENDING).order_by("created_at")
    for notification in notifications:
        try:
            Notification.objects.execute_notification(notification)
        except Exception as ex:
            result_db = notification.result
            if result_db:
                try:
                    result_dict = json.loads(result_db)
                    result_dict["messages"] += f"ERROR NAME {type(ex).__name__}, args: {ex.args}"
                    notification.result = json.dumps(result_dict)
                    notification.save()
                except:
                    pass
