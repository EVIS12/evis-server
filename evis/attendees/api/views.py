from rest_framework import viewsets

from evis.attendees.api.serializers import AttendeesSerializer, CPDSerializer
from evis.attendees.models import CPD, Attendees


class AttendeesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Attendees.objects.all()
    serializer_class = AttendeesSerializer


class CPDViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CPD.objects.all()
    serializer_class = CPDSerializer
