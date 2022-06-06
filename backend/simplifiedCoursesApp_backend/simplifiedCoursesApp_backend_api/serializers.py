from rest_framework import serializers
from .models import TestModel
class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ["task", "completed", "timestamp", "updated", "user"]