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
    order_by = filters.OrderingFilter(
        fields=(
            ("name", "name"),
            ("version__year", "year"),
            ("country", "country"),
        )
    )
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    year = filters.CharFilter(field_name="version__year", lookup_expr="icontains")
    is_partner = filters.BooleanFilter(field_name="is_partner")
    is_sponser = filters.BooleanFilter(field_name="is_sponser")
    slider = filters.BooleanFilter(field_name="slider")
    country = filters.CharFilter(field_name="country", lookup_expr="icontains")

    class Meta:
        model = Exhibitor
        fields = ["name", "year", "is_partner", "is_sponser", "slider", "country"]
