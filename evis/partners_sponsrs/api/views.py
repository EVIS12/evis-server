from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from evis.partners_sponsrs.api.serializers import PartnerAndSponserSerializer
from evis.partners_sponsrs.filters import PartnerSponserFilter
from evis.partners_sponsrs.models import PartnerAndSponser


class PartnerAndSponserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PartnerAndSponser.objects.all()
    serializer_class = PartnerAndSponserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PartnerSponserFilter
