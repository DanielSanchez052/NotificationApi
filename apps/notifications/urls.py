from django.urls import path

from .views import GetNotificationType, GetNotificationStatus

urlpatterns = [
    path('notification_type/',
         GetNotificationType.as_view(), name='notificationType'),
    path('notification_status/', GetNotificationStatus.as_view(),
         name='notificationStatus')
]
