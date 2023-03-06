from django import forms
from apps.notifications.models import Notification, NotificationType


class NotificationAdminForm (forms.ModelForm):
    # notification_type = forms.ModelChoiceField()

    class Meta:
        model = Notification
        fields = [
            'user', 'notification_status', 'notification_type', 'name', 'description', 'result', 'config']

    class Media:
        js = ('js/notification_admin.js',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['notification_type'].widget.attrs.update({
            "onchange": "()=>{console.log('whats up')}"
        })


class NotificationTypeAdminForm (forms.ModelForm):
    class Meta:
        model = NotificationType
        fields = [
            "name", "config", "config_schema", "is_active"
        ]
