from rest_framework import serializers

from evis.exhibitor.models import Exhibitor, ExhibitorVersion, Participant, WhyExhibit, WhyToAttendEvis


class ExhibitorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibitor
        exclude = ["version"]


class ExhibitorVersionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitorVersion
        exclude = ["photo"]


class ExhibitorVersionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitorVersion
        fields = "__all__"


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
