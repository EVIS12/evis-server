# serializers.py
from rest_framework import serializers

from evis.awards.models import StudentProject


class StudentProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProject
        fields = "__all__"
