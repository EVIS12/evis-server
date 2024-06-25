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
        if attrs["is_partner"] and Exhibitor.objects.filter(is_partner=True).count() >= 9:
            raise serializers.ValidationError("Exhibitor has the maximum limit of Partners.")
        elif attrs["is_sponser"] and Exhibitor.objects.filter(is_sponser=True).count() >= 9:
            raise serializers.ValidationError("Exhibitor has the maximum limit of Sponsers.")
        elif attrs["slider"] and Exhibitor.objects.filter(slider=True).count() >= 9:
            raise serializers.ValidationError("Exhibitor has the maximum limit of Slider.")
        return attrs


class ExhibitorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibitor
        fields = "__all__"

    def update(self, instance, validated_data):
        if validated_data.get("is_partner"):
            if Exhibitor.objects.filter(is_partner=True).count() >= 9:
                raise serializers.ValidationError("Exhibitor has the maximum limit of Partners.")
        elif validated_data.get("is_sponser"):
            if Exhibitor.objects.filter(is_sponser=True).count() >= 9:
                raise serializers.ValidationError("Exhibitor has the maximum limit of Sponsers.")
        elif validated_data.get("slider"):
            if Exhibitor.objects.filter(slider=True).count() >= 9:
                raise serializers.ValidationError("Exhibitor has the maximum limit of Slider.")
        return super().update(instance, validated_data)


class ExhibitorDetailSerializer(serializers.ModelSerializer):
    version = serializers.SerializerMethodField()

    class Meta:
        model = Exhibitor
        fields = "__all__"

    def get_version(self, obj: Exhibitor):
        return [version.year for version in obj.version.all()]


class ExhibitorVersionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitorVersion
        fields = ("id", "name", "photo", "year")


class ExhibitorSlider(serializers.ModelSerializer):
    class Meta:
        model = Exhibitor
        fields = ("id", "logo", "sponserShipTitle")


class OrganizersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizers
        fields = ("id", "logo")
