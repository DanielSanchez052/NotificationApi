from abc import ABC, abstractmethod
from typing import Dict


class Strategy (ABC):

    @abstractmethod
    def do_notification(self, settings: Dict, *args, **kwargs):
        pass


CONFIGURATION_SCHEMA_BASE = {
    "strategy": "string",
    "required": ["strategy"]
}
