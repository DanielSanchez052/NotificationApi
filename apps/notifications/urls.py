from django.urls import path

from .views import GetNotificationType, GetNotificationStatus, NotificationView

urlpatterns = [
    path('notification_type/',
         GetNotificationType.as_view(), name='notificationType'),
    path('notification_status/', GetNotificationStatus.as_view(),
         name='notificationStatus'),
    path('notification/', NotificationView.as_view(), name="notification")
]
