from rest_framework import serializers

from apps.notifications.models import Notification
from apps.core.serializers import DefaultResponse


class NotificationSerializer(serializers.ModelSerializer):
    config = serializers.DictField(child=serializers.CharField())
    result = DefaultResponse(required=False, allow_null=True)

    class Meta:
        model = Notification
        fields = ["id", "description", "user",
                  "notification_type", "config", "result"]
        read_only_fields = ("result", "id",)

    def create(self, validated_data):
        validated_data["notification_status"] = Notification.NotificationStatus.MANUAL
        instance = super().create(validated_data)
        new_instance = Notification.objects.execute_notification(instance)
        return new_instance


class NotificationSerializerQueueList(serializers.ListSerializer):
    def create(self, validated_data):
        notification_data = [Notification(**item) for item in validated_data]
        return Notification.objects.bulk_create(notification_data)


class NotificationSerializerQueue(serializers.ModelSerializer):
    config = serializers.DictField(child=serializers.CharField())

    class Meta:
        model = Notification
        fields = ["id", "description", "user",
                  "notification_type", "config"]
        read_only_fields = ("id",)
        list_serializer_class = NotificationSerializerQueueList
