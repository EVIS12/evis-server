from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from evis.exhibitor.filters import ExhibitorFilter, ParticipantFilter
from evis.exhibitor.models import Exhibitor, Organizers, Participant, WhyExhibit, WhyToAttendEvis
from evis.exhibitor.pagination import ParticipantPagination, WhyExhibitPagination, WhyToAttendEvisPagination

from .serializers import (
    ExhibitorListSerializer,
    ExhibitorUpdateSerializer,
    OrganizersSerializer,
    ParticipantSerializer,
    WhyExhibitSerializer,
    WhyToAttendEvisSerializer,
)


class ParticipantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    pagination_class = ParticipantPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ParticipantFilter


class ExhibitorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exhibitor.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ExhibitorFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return ExhibitorListSerializer
        return ExhibitorUpdateSerializer


class WhyExhibitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WhyExhibit.objects.all()
    serializer_class = WhyExhibitSerializer
    pagination_class = WhyExhibitPagination


class WhyToAttendEvisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WhyToAttendEvis.objects.all()
    serializer_class = WhyToAttendEvisSerializer
    pagination_class = WhyToAttendEvisPagination


class OrganizersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organizers.objects.all()
    serializer_class = OrganizersSerializer
    # pagination_class = OrganizersPagination
