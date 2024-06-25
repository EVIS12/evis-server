from rest_framework import viewsets

from evis.speakers.models import Advisors
from evis.speakers.paginations import LargPagination, SmallPagination

from .serializers import AdvisorDetailSerializer, AdvisorListSerializer


class AdvisorsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advisors.objects.all()
    serializer_class = AdvisorListSerializer
    pagination_class = LargPagination

    def get_serializer_class(self):
        if self.action == "list":
            return AdvisorListSerializer
        elif self.action == "retrieve":
            return AdvisorDetailSerializer
        return AdvisorListSerializer


class AdvisorsBoardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advisors.objects.filter(about_page=True)
    serializer_class = AdvisorListSerializer
    pagination_class = SmallPagination

    def get_serializer_class(self):
        if self.action == "list":
            return AdvisorListSerializer
        elif self.action == "retrieve":
            return AdvisorDetailSerializer
        return AdvisorListSerializer
