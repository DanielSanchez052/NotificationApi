
from rest_framework import serializers

from apps.notifications.models import NotificationType, NotificationTemplate


class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = ['id', 'name', 'config', 'config_schema']


class NotificationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = ['id', 'name', 'description', 'template_path', 'render']


class NotificationStatusSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=255)
