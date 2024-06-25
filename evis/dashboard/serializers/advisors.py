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
            "home_page",
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
            "home_page",
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
            "home_page",
            "facebook",
            "twitter",
            "linkedin",
        ]

    def validate(self, attrs):
        if attrs["home_page"] and Advisors.objects.filter(home_page=True).count() >= 10:
            raise serializers.ValidationError("Home Page has the maximum limit of Advisors.")
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
            "home_page",
            "facebook",
            "twitter",
            "linkedin",
        ]

    def validate(self, attrs):
        try:
            if attrs["home_page"] and Advisors.objects.filter(home_page=True).count() >= 10:
                raise serializers.ValidationError("Home Page has the maximum limit of Advisors.")
        except KeyError:
            pass
        return attrs
