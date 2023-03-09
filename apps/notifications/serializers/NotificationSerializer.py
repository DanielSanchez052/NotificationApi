from rest_framework import serializers
from django.utils.module_loading import import_string

from apps.notifications.models import Notification
from apps.notifications.strategy.context import Context


class NotificationSerializer(serializers.ModelSerializer):
    config = serializers.DictField(child=serializers.CharField())

    class Meta:
        model = Notification
        fields = ["name", "description", "user",
                  "notification_type", "config", "result"]
        read_only_fields = ("result",)

    def create(self, validated_data):
        validated_data["notification_status"] = Notification.NotificationStatus.MANUAL

        instance = super().create(validated_data)
        new_instance = Notification.objects.execute_notification(instance)
        return new_instance
