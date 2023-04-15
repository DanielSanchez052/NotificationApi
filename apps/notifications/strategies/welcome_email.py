from typing import Dict
from django.template.loader import render_to_string

from ..strategy.strategy import Strategy
from apps.core.utils import send_email
from apps.core.exeptions import NotificationException


class WelcomeEmailStrategy(Strategy):
    def do_notification(self, settings: Dict, *args, **kwargs):
        self.validate_required_fields(self, settings)
        notification = kwargs["notification"]

        notification_settings = notification.notification_type.config

        email = settings["email"]
        name = settings["name"]
        password = settings["password"]

        context = {
            name: name,
            password: password}

        html_message = render_to_string(
            notification_settings["html_template"], context)

        result = send_email(
            f"Welcome {name} To application",
            [email],
            '',
            html_message
        )

        return result

    def validate_required_fields(self, settings: Dict):
        fields_required = ["name", "email", "password"]
        if not all(field in fields_required for field in settings.keys()):
            raise NotificationException(
                message="el name, email y password son campos requeridos")
