import json
from django.contrib import admin
from apps.notifications.models import Notification, NotificationType
from .forms import NotificationAdminForm, NotificationTypeAdminForm

from .strategy.strategy import CONFIGURATION_SCHEMA_BASE

# admin.site.register(Notification)


@admin.register(NotificationType)
class NotificationTypeModelAdmin(admin.ModelAdmin):
    form = NotificationTypeAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['config'].initial = CONFIGURATION_SCHEMA_BASE
        form.base_fields['config_schema'].initial = CONFIGURATION_SCHEMA_BASE
        return form


@admin.register(Notification)
class NotificationModelAdmin(admin.ModelAdmin):
    form = NotificationAdminForm
