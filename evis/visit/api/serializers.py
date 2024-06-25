from rest_framework import serializers

from evis.visit.models import Visit, WhyVisit


class BaseVisitSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ("id",)

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in self.Meta.fields:
            setattr(instance, field, validated_data.get(field, getattr(instance, field)))
        instance.save()
        return instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["title"] = response["title"].title()
        response["description"] = response["description"].title()
        return response


class VisitSerializer(BaseVisitSerializer):
    class Meta(BaseVisitSerializer.Meta):
        model = Visit
        fields = ("id", "title", "description", "photo")


class WhyVisitSerializer(BaseVisitSerializer):
    class Meta(BaseVisitSerializer.Meta):
        model = WhyVisit
        fields = ("id", "title", "description", "photo")
