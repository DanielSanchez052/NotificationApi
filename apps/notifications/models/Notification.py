import uuid

from django.utils.module_loading import import_string
from django.core.exceptions import ValidationError as Error
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from .NotificationType import NotificationType
from apps.notifications.strategy.context import Context


class NotificationManager(models.Manager):
    def execute_notification(self, notification, *args, **kwargs):
        notificationDb = self.get(id=notification.id)
        try:
            result = notificationDb.execute_notification()

            notificationDb.result = f"Success: {result}"
            notificationDb.notification_status = Notification.NotificationStatus.COMPLETE
        except Exception as ex:
            notificationDb.result = f"ERROR NAME {type(ex).__name__}, args: {ex.args}"
            notificationDb.notification_status = Notification.NotificationStatus.CANCELED

        finally:
            notificationDb.save()

        return notificationDb


class Notification(BaseModel):

    class NotificationStatus(models.TextChoices):
        PENDING = "PENDING", _("PENDING")
        CANCELED = "CANCELED", _("CANCELED")
        MANUAL = "MANUAL", _("MANUAL")
        COMPLETE = "COMPLETE", _("COMPLETED")
        IN_PROCESS = "IN_PROCESS", _("IN PROCESS")

        __empty__ = ('(unknown)')

        def __str__(self) -> str:
            return f'{self.name}'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField(max_length=255, blank=True, null=False)
    user = models.UUIDField(blank=True, null=True)
    notification_status = models.CharField(
        max_length=20,
        choices=NotificationStatus.choices,
        default=NotificationStatus.PENDING)
    notification_type = models.ForeignKey(
        NotificationType, on_delete=models.CASCADE)
    result = models.TextField(max_length=255, blank=True, null=True)
    config = models.JSONField(
        'config', blank=False, null=False)
    objects = NotificationManager()

    def __str__(self) -> str:
        return f'{self.id}|{self.name}|{self.notification_status}|{self.result}'

    class Meta:
        ordering = ["created_at"]
        verbose_name = 'Notification'
        verbose_name_plural = 'Notification'

    def execute_notification(self):
        if self.notification_status == self.NotificationStatus.COMPLETE or \
                self.notification_status == self.NotificationStatus.IN_PROCESS:
            return

        notification_startegy = import_string(
            self.notification_type.config["strategy"])

        context = Context(notification_startegy)

        return context.execute_notification(self.config, **self.config)
