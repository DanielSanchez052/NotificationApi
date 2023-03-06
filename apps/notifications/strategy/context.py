import logging
import json
from typing import Dict
from django.conf import settings

from apps.notifications import Notification, NotificationType
from .strategy import Strategy

logger = logging.getLogger(__name__)


class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_notification(self, config, *args, **kwargs) -> None:
        self._strategy.do_notification(self._strategy, config, *args, **kwargs)
