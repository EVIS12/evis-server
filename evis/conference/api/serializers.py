from rest_framework import serializers

from evis.conference.models import AboutConferenceImage, ContractFile, ContractForm


class ContractFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractFile
        fields = "__all__"


class ContractFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractForm
        fields = "__all__"


class AboutConferenceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutConferenceImage
        fields = "__all__"
