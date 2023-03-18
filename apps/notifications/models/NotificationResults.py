import uuid

from django.db import models

from apps.notifications import models as im


class NotificationResults(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    messages = models.TextField()
    error = models.BooleanField(default=False)
    notification = models.ForeignKey(
        im.Notification, on_delete=models.DO_NOTHING, related_name='results')
    created_at = models.DateTimeField(
        'created at', auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Notification Result'
        verbose_name_plural = 'Notification Results'
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.id}|{self.error}|{self.created_at}|{self.messages}"
