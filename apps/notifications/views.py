import json

import django_filters.rest_framework
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.settings import api_settings

from .models import Notification
from .serializers.general_serializer import NotificationTypeSerializer, NotificationStatusSerializer
from .serializers.NotificationSerializer import NotificationSerializer, NotificationSerializerQueue, NotificationUpdateSerializer
from apps.core.mixins import SerializerActionMixin
from apps.core.exeptions import NotificationException
from apps.core.serializers import DefaultResponse


class GetNotificationType(ListAPIView):
    serializer_class = NotificationTypeSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)


class GetNotificationStatus(ListAPIView):
    serializer_class = NotificationStatusSerializer
    object_list = Notification.NotificationStatus

    def list(self, request, *args, **kwagrs):
        objects = list(
            map(lambda item: (
                {'id': item.value, 'name': item.name}), self.object_list)
        )
        serializer = self.get_serializer(objects, many=True)

        return Response(serializer.data)


class NotificationQueueView(SerializerActionMixin, viewsets.GenericViewSet):
    serializer_classes = {
        "execute_notification": NotificationSerializer,
        "queue_notification": NotificationSerializerQueue
    }
    queryset = Notification.objects.all()

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)

    @action(methods=["post"], detail=False, url_path=r"enqueue")
    def queue_notification(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as ex:
            print(ex)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["post"], detail=True, url_path=r"execute-notification")
    def execute_notification(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            # update Notification
            update_serializer = NotificationUpdateSerializer(
                instance, data=request.data)
            update_serializer.is_valid(raise_exception=True)
            updated = update_serializer.save()

            # execute notification
            notification = Notification.objects.execute_notification(updated)
            serializer = self.get_serializer(notification)
            return Response(serializer.data)

        except NotificationException as ne:
            response = {
                "error": True,
                "messages": [
                    str(ne.message)
                ]
            }
            serialize = DefaultResponse(response)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class NotificationView(SerializerActionMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    serializer_class = NotificationSerializer
    filterset_fields = ['notification_status', 'user', 'notification_type']
    queryset = Notification.objects.all()
