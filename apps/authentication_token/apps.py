from django.apps import AppConfig


class AuthenticationTokenConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.authentication_token"

    def ready(self) -> None:
        import apps.authentication_token.signals
