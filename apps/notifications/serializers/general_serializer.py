
from rest_framework import serializers

from apps.notifications.models import NotificationType


class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = ['id', 'name', 'config', 'config_schema']


class NotificationStatusSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=255)
