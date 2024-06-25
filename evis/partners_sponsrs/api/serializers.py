from rest_framework import serializers

from evis.partners_sponsrs.models import PartnerAndSponser


class PartnerAndSponserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerAndSponser
        fields = "__all__"
        read_only_fields = ("id",)
