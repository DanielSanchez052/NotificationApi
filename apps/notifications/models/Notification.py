import uuid
from jsonschema import validate, ValidationError

from django.core.exceptions import ValidationError as Error
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from .NotificationType import NotificationType
from ..strategy.strategy import CONFIGURATION_SCHEMA_BASE


class Notification(BaseModel):

    class NotificationStatus(models.IntegerChoices):
        PENDING = 0, _("PENDING")
        COMPLETE = 1, _("COMPLETED")
        CANCELED = 2, _("CANCELED")
        IN_PROCESS = 3, _("IN PROCESS")

        __empty__ = ('(unknown)')

        def __str__(self) -> str:
            return f'{self.name}'

        def get(self, index):
            return list(self)[index]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField(max_length=255, blank=True, null=False)
    user = models.UUIDField(blank=True, null=True)
    notification_status = models.IntegerField(
        choices=NotificationStatus.choices, default=NotificationStatus.PENDING)
    notification_type = models.ForeignKey(
        NotificationType, on_delete=models.CASCADE)
    result = models.TextField(max_length=255, blank=True, null=True)
    config = models.JSONField(
        'config', blank=False, null=False)

    def __str__(self) -> str:
        return f'{self.id}|{self.name}|{self.notification_status_name}|{self.result}'

    @property
    def notification_status_name(self):
        return self.NotificationStatus.get(self.NotificationStatus, self.notification_status)

    class Meta:
        ordering = ["created_at"]
        verbose_name = 'Notification'
        verbose_name_plural = 'Notification'

    def clean(self):
        try:
            config_value = self.config
            schema = self.notification_type.config_schema

            if not schema:
                schema = CONFIGURATION_SCHEMA_BASE

            validate(config_value, schema)
        except ValidationError as e:
            raise Error({"config": (e.message)})
        except Exception as e:
            raise Error(
                {"config": (f"Error: {e.args}")}, code="invalid")
