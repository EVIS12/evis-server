from rest_framework import serializers

from evis.conference.models import AboutConferenceImage, ContractFile


class ConferenceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutConferenceImage
        fields = "__all__"


class ConferenceImageCreateSerializer(serializers.ModelSerializer):
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True,
    )

    class Meta:
        model = AboutConferenceImage
        fields = ["uploaded_images"]

    def create(self, validated_data):
        images = validated_data.pop("uploaded_images")
        created_images = []

        for image in images:
            created_images.append(AboutConferenceImage.objects.create(image=image))

        return created_images


class ContractFileListSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = ContractFile
        fields = "__all__"

    def get_file_name(self, obj):
        return obj.file.name.split("/")[-1]


class ContractFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractFile
        fields = "__all__"

    def validate(self, attrs):
        if ContractFile.objects.all().count() >= 8:
            raise serializers.ValidationError("You can only upload 8 files")
        return attrs


class ContractFileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractFile
        fields = "__all__"
