from django.db import models
from ..validators import ConfigDefaultValidator


class NotificationType(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=True)
    config = models.JSONField(
        'config_default', max_length=500, blank=False, null=False, validators=[
            ConfigDefaultValidator
        ])
    config_schema = models.JSONField(
        'config_schema', max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}|{self.is_active}'

    class Meta:
        verbose_name = 'Notification Type'
        verbose_name_plural = 'Notification Type'
