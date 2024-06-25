from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from evis.speakers.models import Advisors

from .filters import AdvisorsFilter
from .serializers import AdvisorDetailSerializer, AdvisorListSerializer


class AdvisorsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advisors.objects.all()
    serializer_class = AdvisorListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvisorsFilter

    def get_serializer_class(self):
        if self.action == "list":
            return AdvisorListSerializer
        elif self.action == "retrieve":
            return AdvisorDetailSerializer
        return AdvisorListSerializer


class AdvisorsBoardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advisors.objects.filter(home_page=True)
    serializer_class = AdvisorListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return AdvisorListSerializer
        elif self.action == "retrieve":
            return AdvisorDetailSerializer
        return AdvisorListSerializer
