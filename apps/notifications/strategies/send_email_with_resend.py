from typing import Dict
from django.template.loader import render_to_string

from ..strategy.strategy import Strategy
from apps.core.exeptions import NotificationException
from apps.notifications.models import Notification
import resend

class SendEmailWithConfig(Strategy):
    def do_notification(self, settings: Dict, *args, **kwargs):
        self.validate_required_fields(self, settings)

        notification: Notification = kwargs["notification"]
        notification_settings: Dict = notification.notification_type.config

        resend.api_key = notification_settings.get("API_KEY")
        
        template = notification.notification_template

        message = ""
        if (template.render):
            message = render_to_string(template.template_path, settings)
        else:
            # TODO:Review this and test if here i can read file and send his content
            message = template.template_path

        params = {
            "from": notification_settings.get("FROM"),
            "to": [settings["email"]],
            "subject": settings["subject"],
            "html": message
        }

        return resend.Emails.send(params)

    def validate_required_fields(self, settings: Dict):
        fields_required = ["email", "subject"]
        if not all(field in settings.keys() for field in fields_required):
            raise NotificationException(
                message="el email y el asunto son requeridos")

