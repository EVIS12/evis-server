from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from evis.exhibitor.filters import ExhibitorFilter, ExhibitorVersionFilter, ParticipantFilter
from evis.exhibitor.models import Exhibitor, ExhibitorVersion, Organizers, Participant, WhyExhibit, WhyToAttendEvis
from evis.exhibitor.pagination import (
    ExhibitorPagination,
    ExhibitorVersionPagination,
    OrganizersPagination,
    ParticipantPagination,
    WhyExhibitPagination,
    WhyToAttendEvisPagination,
)

from .serializers import (
    ExhibitorDetailSerializer,
    ExhibitorListSerializer,
    ExhibitorSlider,
    ExhibitorVersionListSerializer,
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


class ExhibitorVersionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExhibitorVersion.objects.all()
    serializer_class = ExhibitorVersionListSerializer
    pagination_class = ExhibitorVersionPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExhibitorVersionFilter


class ExhibitorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exhibitor.objects.all()
    pagination_class = ExhibitorPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ExhibitorFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return ExhibitorListSerializer
        return ExhibitorDetailSerializer


class ExhibitorSliderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exhibitor.objects.all()
    serializer_class = ExhibitorSlider
    pagination_class = ExhibitorPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExhibitorFilter


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
    pagination_class = OrganizersPagination
