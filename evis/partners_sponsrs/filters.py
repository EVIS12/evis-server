from django_filters import rest_framework as filters

from evis.partners_sponsrs.models import PartnerAndSponser


class PartnerSponserFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="category__name", lookup_expr="icontains")

    class Meta:
        model = PartnerAndSponser
        fields = ["category"]
