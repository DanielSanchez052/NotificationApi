from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.notifications.models import Notification, NotificationType
from .forms import NotificationAdminForm, NotificationTypeAdminForm
from .strategy.strategy import CONFIGURATION_SCHEMA_BASE


class NotificationTypeResource(resources.ModelResource):
    class Meta:
        model = NotificationType


class NotificationResource(resources.ModelResource):
    class Meta:
        model = Notification


@admin.register(NotificationType)
class NotificationTypeModelAdmin(ImportExportModelAdmin):
    form = NotificationTypeAdminForm
    resource_classes = [NotificationTypeResource]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['config'].initial = CONFIGURATION_SCHEMA_BASE
        form.base_fields['config_schema'].initial = CONFIGURATION_SCHEMA_BASE
        return form


@admin.register(Notification)
class NotificationModelAdmin(admin.ModelAdmin):
    form = NotificationAdminForm
    resource_classes = [NotificationResource]
