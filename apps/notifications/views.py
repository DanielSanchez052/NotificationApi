from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView

from .models import Notification
from .serializers.general_serializer import NotificationTypeSerializer, NotificationStatusSerializer
from .serializers.NotificationSerializer import NotificationSerializer


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


class NotificationView(mixins.CreateModelMixin, GenericAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
