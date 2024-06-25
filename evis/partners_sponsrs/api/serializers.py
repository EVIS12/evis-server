from rest_framework import serializers

from evis.partners_sponsrs.models import Categorty, PartnerAndSponser


class PartnerAndSponserCUSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerAndSponser
        fields = "__all__"


class PartnerAndSponserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerAndSponser
        exclude = ("category",)


class PartnerAndSponserDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = PartnerAndSponser
        fields = "__all__"
        read_only_fields = ("id",)

    def get_category(self, obj: PartnerAndSponser):
        return [category.name for category in obj.category.all()]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorty
        fields = "__all__"


class CategorySPSerializer(serializers.ModelSerializer):
    sponsers_partners = serializers.SerializerMethodField()

    class Meta:
        model = Categorty
        fields = "__all__"

    def get_sponsers_partners(self, obj: Categorty):
        # return list of sponsers and partners for each category
        sponsers_partners = PartnerAndSponser.objects.filter(category=obj)
        return PartnerAndSponserListSerializer(sponsers_partners, many=True).data
