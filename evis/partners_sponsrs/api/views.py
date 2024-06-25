from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from evis.partners_sponsrs.api.serializers import (
    CategorySerializer,
    PartnerAndSponserDetailSerializer,
    PartnerAndSponserListSerializer,
)
from evis.partners_sponsrs.filters import PartnerSponserFilter
from evis.partners_sponsrs.models import Categorty, PartnerAndSponser


class PartnerAndSponserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PartnerAndSponser.objects.all()
    serializer_class = PartnerAndSponserListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PartnerSponserFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PartnerAndSponserDetailSerializer
        return PartnerAndSponserListSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categorty.objects.all()
    serializer_class = CategorySerializer
