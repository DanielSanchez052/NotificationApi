from rest_framework import serializers


class DefaultResponse(serializers.Serializer):
    message = serializers.CharField(max_length=500)
    status_code = serializers.IntegerField()
