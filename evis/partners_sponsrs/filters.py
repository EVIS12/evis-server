from django_filters import rest_framework as filters

from evis.partners_sponsrs.models import Categorty, PartnerAndSponser


class PartnerSponserFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="category", lookup_expr="icontains")

    class Meta:
        model = PartnerAndSponser
        fields = ["category"]


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Categorty
        fields = ["name"]
