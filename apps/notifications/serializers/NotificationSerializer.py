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
        try:
            validated_data["notification_status"] = Notification.NotificationStatus.COMPLETE

            result = self.execute_notification(
                validated_data, validated_data["config"])
            validated_data["result"] = f"Success: {result}"
        except KeyError as ke:
            validated_data[
                "result"] = f"Ha ocurrido un error al tratar de obtener la informacion de {ke}"
            validated_data["notification_status"] = Notification.NotificationStatus.CANCELED
        except Exception as ex:
            validated_data["result"] = f"Ha ocurrido un error inesperado {ex}"
            Notification.NotificationStatus.CANCELED

        return super().create(validated_data)

    def execute_notification(self, data, *args, **kwargs):
        config = data["notification_type"].config

        notification_startegy = import_string(config["strategy"])

        context = Context(notification_startegy)

        return context.execute_notification(config, *args, **kwargs)
