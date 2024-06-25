from rest_framework import serializers

from evis.attendees.models import CPD, Attendees


class AttendeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendees
        fields = "__all__"


class CPDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPD
        exclude = ("created_at",)
