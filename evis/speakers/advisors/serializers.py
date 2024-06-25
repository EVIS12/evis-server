from rest_framework import serializers

from evis.speakers.models import Advisors


class AdvisorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisors
        fields = ["id", "name", "job_title", "description", "photo", "home_page", "company"]


class AdvisorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisors
        fields = "__all__"
