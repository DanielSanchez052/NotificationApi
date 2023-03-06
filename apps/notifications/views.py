from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Notification
from .serializers.general_serializer import NotificationTypeSerializer, NotificationStatusSerializer


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
