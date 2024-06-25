from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from evis.partners_sponsrs.api.serializers import (
    CategorySerializer,
    CategorySPSerializer,
    PartnerAndSponserDetailSerializer,
)
from evis.partners_sponsrs.filters import CategoryFilter, PartnerSponserFilter
from evis.partners_sponsrs.models import Categorty, PartnerAndSponser


class PartnerAndSponserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PartnerAndSponser.objects.all()
    serializer_class = PartnerAndSponserDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PartnerSponserFilter


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categorty.objects.all()
    serializer_class = CategorySerializer


class PartnerSponsersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categorty.objects.all()
    serializer_class = CategorySPSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter
