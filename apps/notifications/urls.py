from rest_framework import routers
from django.urls import path

from .views import GetNotificationType, GetNotificationStatus, NotificationView, NotificationQueueView, GetNotificationTemplate

router = routers.DefaultRouter()
router.register(r'notification', NotificationQueueView, basename='notification_queue')
router.register(r'notification', NotificationView, basename='notification')


urlpatterns = [
    path('notification_type/', GetNotificationType.as_view(), name='list_notification_type'),
    path('notification_status/', GetNotificationStatus.as_view(), name='list_notification_status'),
    path('notification_template/', GetNotificationTemplate().as_view(), name='list_notification_template'),
] + router.urls
