from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.notifications.models import Notification, NotificationType, NotificationResults
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


@admin.register(NotificationResults)
class NotificationResultsAdmin(admin.ModelAdmin):
    list_filter = ("error",)


class ResultsInline(admin.TabularInline):
    model = NotificationResults


@admin.register(Notification)
class NotificationModelAdmin(admin.ModelAdmin):
    search_fields = ["id", "description", "user"]
    list_filter = ("id", "notification_status")
    form = NotificationAdminForm
    resource_classes = [NotificationResource]
    inlines = [ResultsInline]
    actions = ["change_to_pending"]

    @admin.action(description="Change Nototifications status to pending")
    def change_to_pending(self, request, queryset):
        queryset.update(
            notification_status=Notification.NotificationStatus.PENDING)
