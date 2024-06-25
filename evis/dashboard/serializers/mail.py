from rest_framework import serializers

from evis.dashboard.models import Mail


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = "__all__"
