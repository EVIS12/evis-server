from rest_framework import serializers

from evis.exhibitor.models import Exhibitor, Organizers, Participant, WhyExhibit, WhyToAttendEvis


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

    def validate(self, attrs):
        try:
            if WhyExhibit.objects.all().count() >= 3:
                raise serializers.ValidationError("Why Exhibit has the maximum limit of items")
        except Exception:
            pass
        return attrs


class WhyToAttendEvisSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = WhyToAttendEvis

    def validate(self, attrs):
        try:
            if WhyToAttendEvis.objects.all().count() >= 3:
                raise serializers.ValidationError("Why Attend has the maximum limit of items")
        except Exception:
            pass
        return attrs


class ExhibitorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibitor
        fields = ["id", "name", "logo", "description", "standNumber"]


class ExhibitorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibitor
        fields = "__all__"

    def validate(self, attrs):
        if Exhibitor.objects.all().count() >= 30:
            raise serializers.ValidationError("Exhibitor has the maximum limit of items")
        return attrs


class ExhibitorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibitor
        fields = "__all__"


class OrganizersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizers
        fields = ("id", "logo")
