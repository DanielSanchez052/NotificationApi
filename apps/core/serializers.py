import json
from ast import literal_eval

from rest_framework import serializers


class DefaultResponse(serializers.Serializer):
    messages = serializers.ListField(
        child=serializers.CharField()
    )
    error = serializers.BooleanField(default=False)

    def to_representation(self, instance):
        if isinstance(instance, str):
            instance = literal_eval(instance)
        return super().to_representation(instance)
