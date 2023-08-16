from django.db import models
from apps.core.models import BaseModel


class NotificationTemplate(BaseModel):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=255, blank=True, null=False)
    template_path = models.TextField(max_length=255, blank=False, null=False)
    render = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'NotificationTemplate'
        verbose_name_plural = 'NotificationTemplates'

    def __str__(self):
        return self.name
