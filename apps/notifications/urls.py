from rest_framework import routers
from django.urls import path

from .views import GetNotificationType, GetNotificationStatus, NotificationView

router = routers.DefaultRouter()
router.register(r'notification', NotificationView, basename='notification')


urlpatterns = [
    path('notification_type/',
         GetNotificationType.as_view(), name='notificationType'),
    path('notification_status/', GetNotificationStatus.as_view(),
         name='notificationStatus'),
] + router.urls
