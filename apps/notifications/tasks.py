import json
from datetime import datetime

from django.conf import settings

from celery import shared_task, Task
from celery.utils.log import get_task_logger

from apps.notifications.models import Notification, NotificationResults


logger = get_task_logger(__name__)


class TaskLogs(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error('{0!r} failed: {1!r}'.format(task_id, exc))
        return super().on_failure(exc, task_id, args, kwargs, einfo)

    def on_success(self, retval, task_id, args, kwargs):
        logger.info('{0!r} Success: {1!r}'.format(task_id, retval))
        return super().on_success(retval, task_id, args, kwargs)


@shared_task(name="run_queued_notifications", base=TaskLogs)
def run_notifications():
    # execute notifications in pending
    logger.info(f"Start run notification queued task")
    
    notifications = Notification.objects.filter(
        notification_status=Notification.NotificationStatus.PENDING).order_by("created_at")[:settings.NOTIFICATIONS_QUEUE_BATCH]
    
    for notification in notifications:
        try:
            Notification.objects.execute_notification(notification)
            
        except Exception as ex:
            result_db = notification.result
            if result_db:
                result = NotificationResults()
                result.error = True
                result.created_at = datetime.now()
                result.messages = f"ERROR NAME {type(ex).__name__}, args: {ex.args}, {ex}"
                result.notification = notification

                notification.save()
                result.save()
                
    return notifications.count()
