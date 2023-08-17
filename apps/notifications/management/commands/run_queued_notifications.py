import json
import logging
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.conf import settings

from apps.notifications.models import Notification, NotificationResults


class Command(BaseCommand):
    help = "get pending notifications and execute them"

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('-b', '--batch', type=int, help="how much notifications process in every execute")

    def handle(self, *args, **kwargs):
        batch = kwargs["batch"]
        print(f"Start -> {datetime.now()} -> Run Queued notifications -> batch {batch}")
        if not batch:
            batch = settings.NOTIFICATIONS_QUEUE_BATCH

        notifications = Notification.objects.filter(
            notification_status=Notification.NotificationStatus.PENDING).order_by("created_at")[:]

        for notification in notifications:
            try:
                Notification.objects.execute_notification(notification)

            except Exception as ex:
                result_db = notification.results
                if result_db:
                    result = NotificationResults()
                    result.error = True
                    result.created_at = datetime.now()
                    result.messages = f"ERROR NAME {type(ex).__name__}, args: {ex.args}, {ex}"
                    result.notification = notification

                    notification.save()
                    result.save()

        notifications_pending = notifications.count()

        print(f"End -> {datetime.now()} -> End of Queued notifications -> {notifications_pending}")
