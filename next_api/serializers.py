#serializers.py

from rest_framework import serializers

class JobSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description=serializers.CharField(max_length=500)
    company = serializers.CharField(max_length=255)
    logo = serializers.URLField()
    location = serializers.CharField(max_length=255)
    link = serializers.URLField()
