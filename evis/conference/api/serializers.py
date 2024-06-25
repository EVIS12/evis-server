from rest_framework import serializers

from evis.conference.models import AboutConferenceImage, ContractFile, ContractForm


class ContractFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractFile
        fields = "__all__"


class ContractFormAdminSerializer(serializers.ModelSerializer):
    contract_file = serializers.SerializerMethodField()

    class Meta:
        model = ContractForm
        fields = "__all__"

    def get_contract_file(self, obj):
        contract_file = obj.contract_file.all()
        return [file.type for file in contract_file]


class ContractFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractForm
        fields = "__all__"


class AboutConferenceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutConferenceImage
        fields = "__all__"
