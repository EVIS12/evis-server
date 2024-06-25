from rest_framework import serializers

from evis.speakers.models import Speakers, SpeakersVersion


class SpeakerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = ["id", "name", "job_title", "description", "photo", "conference_page", "home_page", "company"]


class SpeakerDetailSerializer(serializers.ModelSerializer):
    version = serializers.SerializerMethodField()

    class Meta:
        model = Speakers
        fields = [
            "id",
            "photo",
            "name",
            "job_title",
            "company",
            "description",
            "country",
            "facebook",
            "twitter",
            "linkedin",
            "created_at",
            "home_page",
            "conference_page",
            "version",
        ]

    def get_version(self, obj: Speakers):
        return [version.year for version in obj.version.all()]


class SpeakerVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakersVersion
        fields = "__all__"
