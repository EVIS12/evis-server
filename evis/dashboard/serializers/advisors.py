from rest_framework import serializers

from evis.speakers.models import Advisors


class AdvisorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisors
        fields = [
            "id",
            "photo",
            "name",
            "job_title",
            "about_page",
        ]


class AdvisorsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisors
        fields = [
            "id",
            "photo",
            "name",
            "job_title",
            "description",
            "company",
            "about_page",
            "facebook",
            "twitter",
            "linkedin",
        ]


class AdvisorsCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisors
        fields = [
            "id",
            "photo",
            "name",
            "job_title",
            "description",
            "company",
            "about_page",
            "facebook",
            "twitter",
            "linkedin",
        ]
