from django.core.exceptions import ValidationError as Error

from .strategy.strategy import CONFIGURATION_SCHEMA_BASE

from jsonschema import validate, ValidationError


def ConfigDefaultValidator(value):
    config_schema = CONFIGURATION_SCHEMA_BASE
    try:
        validate(value, config_schema)

    except ValidationError as v:
        raise Error(v.message, code='config')
