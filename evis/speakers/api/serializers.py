from rest_framework import serializers

from evis.speakers.models import Speakers, SpeakersVersion


class SpeakerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = ["id", "name", "job_title", "description", "photo", "conference_page", "home_page"]


class SpeakerDetailSerializer(serializers.ModelSerializer):
    year = serializers.SerializerMethodField()

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
            "year",
        ]

    def get_year(self, obj: Speakers):
        return obj.version.values_list("year")


class SpeakerVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakersVersion
        fields = "__all__"
