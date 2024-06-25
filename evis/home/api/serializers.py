from rest_framework import serializers

from evis.home.models import Contact, Statistic, Timer


class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = "__all__"


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
