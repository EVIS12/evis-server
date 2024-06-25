from rest_framework import serializers

from evis.exhibitor.models import Exhibitor, ExhibitorVersion, Organizers, Participant, WhyExhibit, WhyToAttendEvis


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = "__all__"


class ParticipantSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Participant


class WhyExhibitSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = WhyExhibit


class WhyToAttendEvisSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = WhyToAttendEvis


class ExhibitorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibitor
        fields = ["id", "name", "logo", "description", "standNumber"]


class ExhibitorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibitor
        fields = "__all__"


class ExhibitorVersionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitorVersion
        fields = ("id", "name", "photo", "year")


class ExhibitorSlider(serializers.ModelSerializer):
    class Meta:
        model = Exhibitor
        fields = ("id", "logo")


class OrganizersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizers
        fields = ("id", "logo")
