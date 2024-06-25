from rest_framework import serializers

from evis.speakers.models import Speakers, SpeakersVersion


class SpeakersVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakersVersion
        fields = "__all__"


class SpeakersVersionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakersVersion
        exclude = ["photo"]


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = "__all__"


class SpeakerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = ["id", "name", "job_title", "photo", "conference_page", "home_page"]
