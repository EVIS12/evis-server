from rest_framework import viewsets
from rest_framework.response import Response

from evis.home.models import Contact, Statistic, Timer

from .serializers import ContactSerializer, StatisticSerializer, TimerSerializer


class TimerViewSet(viewsets.ViewSet):
    def list(self, request):
        timer = Timer.get_solo()
        serializer = TimerSerializer(timer)
        return Response(serializer.data)


class StatisticViewSet(viewsets.ViewSet):
    def list(self, request):
        statistic = Statistic.get_solo()
        serializer = StatisticSerializer(statistic)
        return Response(serializer.data)


class ContactViewSet(viewsets.ViewSet):
    def list(self, request):
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)
