from rest_framework import viewsets

from evis.attendees.api.serializers import AttendeesSerializer, CPDSerializer
from evis.attendees.models import CPD, Attendees
from evis.attendees.pagination import AttendeesPagination


class AttendeesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Attendees.objects.all()
    serializer_class = AttendeesSerializer
    pagination_class = AttendeesPagination


class CPDViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CPD.objects.all()
    serializer_class = CPDSerializer
