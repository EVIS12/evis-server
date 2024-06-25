from rest_framework import serializers

from evis.exhibitor.models import Exhibitor, ExhibitorVersion, Participant, WhyExhibit, WhyToAttendEvis


class ExhibitorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibitor
        fields = "__all__"

    def validate(self, attrs):
        try:
            if attrs["slider"] and Exhibitor.objects.filter(slider=True).count() >= 20:
                raise serializers.ValidationError("Slider has the maximum limit of Exhibitors.")
        except KeyError:
            pass
        return attrs


class ExhibitorVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitorVersion
        fields = "__all__"

    def create(self, *args, **kwargs):
        year = self.validated_data.get("year")
        if ExhibitorVersion.objects.filter(year=year).exists():
            raise serializers.ValidationError({"year": "This year is already exist"})
        return super().create(*args, **kwargs)


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = "__all__"


class WhyExhibitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyExhibit
        fields = "__all__"


class WhyToAttendEvisSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyToAttendEvis
        fields = "__all__"
