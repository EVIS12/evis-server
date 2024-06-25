from rest_framework import serializers

from evis.speakers.models import Speakers, SpeakersVersion


class SpeakersVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakersVersion
        fields = "__all__"

    def create(self, *args, **kwargs):
        year = self.validated_data.get("year")
        if SpeakersVersion.objects.filter(year=year).exists():
            raise serializers.ValidationError({"year": "This year is already exist"})
        return super().create(*args, **kwargs)


class SpeakersVersionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakersVersion
        exclude = ["photo"]


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = "__all__"

    def validate(self, attrs):
        try:
            if attrs["home_page"] and Speakers.objects.filter(home_page=True).count() >= 3:
                raise serializers.ValidationError("Home Page has the maximum limit of Speakers.")
            elif attrs["conference_page"] and Speakers.objects.filter(conference_page=True).count() >= 3:
                raise serializers.ValidationError("Conference Page has the maximum limit of Speakers.")
        except Exception:
            pass
        return attrs


class SpeakerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speakers
        fields = ["id", "name", "job_title", "photo", "conference_page", "home_page"]
