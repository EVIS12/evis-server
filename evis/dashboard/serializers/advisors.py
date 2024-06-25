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


class AdvisorsCreateSerializer(serializers.ModelSerializer):
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

    def validate(self, attrs):
        if attrs["about_page"] and Advisors.objects.filter(about_page=True).count() >= 10:
            raise serializers.ValidationError("About Page has the maximum limit of Advisors.")
        return attrs


class AdvisorsUpdateSerializer(serializers.ModelSerializer):
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

    def validate(self, attrs):
        try:
            if attrs["about_page"] and Advisors.objects.filter(about_page=True).count() >= 10:
                raise serializers.ValidationError("About Page has the maximum limit of Advisors.")
        except Exception:
            pass
        return attrs
