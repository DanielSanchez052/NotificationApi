from typing import Dict
from django.template.loader import render_to_string

from ..strategy.strategy import Strategy
from apps.core.utils import EmailSender
from apps.core.exeptions import NotificationException
from apps.notifications.models import Notification


class SendEmailWithConfig(Strategy):
    def do_notification(self, settings: Dict, *args, **kwargs):
        self.validate_required_fields(self, settings)

        notification: Notification = kwargs["notification"]
        notification_settings = notification.notification_type.config

        email_sender = self.get_emailSender(self, notification_settings)
        template = notification.notification_template

        message = ""
        if (template.render):
            message = render_to_string(template.template_path, settings)
        else:
            # TODO:Review this and test if here i can read file and send his content
            message = template.template_path

        email = settings["email"]
        subject = settings["subject"]

        result = email_sender.send_email(
            subject,
            [email],
            '',
            message)

        return result

    def validate_required_fields(self, settings: Dict):
        fields_required = ["email", "subject"]
        if not all(field in settings.keys() for field in fields_required):
            raise NotificationException(
                message="el email y el asunto son requeridos")

    def get_emailSender(self, notification_settings: Dict):
        host = notification_settings.get("host")
        port = notification_settings.get("port")
        username = notification_settings.get("username")
        password = notification_settings.get("password")
        use_tls = notification_settings.get("use_tls")
        use_ssl = notification_settings.get("use_ssl")
        timeout = notification_settings.get("timeout")
        # ssl_keyfile = notification_settings.get("ssl_keyfile")
        # ssl_certfile = notification_settings.get("ssl_certfile")

        return EmailSender(host, port, username, password, use_tls, use_ssl, timeout)
