from ..strategy.strategy import Strategy
from typing import Dict


class WelcomeEmailStrategy(Strategy):
    def do_notification(self, settings: Dict, *args, **kwargs):
        print("Email Sended")
