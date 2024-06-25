from django_filters import rest_framework as filters

from .models import Exhibitor, ExhibitorVersion, Participant


class ParticipantFilter(filters.FilterSet):
    type = filters.CharFilter(field_name="type", lookup_expr="icontains")

    class Meta:
        model = Participant
        fields = ["type"]


class ExhibitorVersionFilter(filters.FilterSet):
    year = filters.NumberFilter(field_name="year", lookup_expr="year")

    class Meta:
        model = ExhibitorVersion
        fields = ["year"]


class ExhibitorFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    version = filters.CharFilter(field_name="version__name", lookup_expr="icontains")
    is_parter = filters.BooleanFilter(field_name="is_parter")
    is_sponser = filters.BooleanFilter(field_name="is_sponser")
    year = filters.NumberFilter(field_name="version__year", lookup_expr="exact")

    class Meta:
        model = Exhibitor
        fields = ["name", "version", "is_parter", "is_sponser", "year"]
