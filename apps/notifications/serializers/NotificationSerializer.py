from rest_framework import serializers
from ast import literal_eval

from apps.notifications.models import Notification, NotificationResults


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationResults
        fields = ["messages", "error", "created_at"]


class NotificationSerializer(serializers.ModelSerializer):
    config = serializers.DictField(child=serializers.CharField())
    results = ResultSerializer(
        read_only=True, many=True)

    class Meta:
        model = Notification
        fields = ["id", "description", "user", "notification_status",
                  "notification_type", "config", "results"]
        read_only_fields = ("results", "id", "notification_status")

    def create(self, validated_data):
        validated_data["notification_status"] = Notification.NotificationStatus.MANUAL
        instance = super().create(validated_data)
        new_instance = Notification.objects.execute_notification(instance)
        return new_instance


class NotificationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["description", "user", "config"]


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
