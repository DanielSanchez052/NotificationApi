from ..strategy.strategy import Strategy
from typing import Dict


class WelcomeEmailStrategy(Strategy):
    def do_notification(self, *args, **kwargs):
        print("Email Sended")
        var1 = kwargs["additionalProp1"]
        return f"Email Sended To {var1}"
