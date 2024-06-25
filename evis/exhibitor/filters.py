from django_filters import rest_framework as filters

from .models import Exhibitor, Participant


class ParticipantFilter(filters.FilterSet):
    type = filters.CharFilter(field_name="type", lookup_expr="icontains")

    class Meta:
        model = Participant
        fields = ["type"]


class ExhibitorFilter(filters.FilterSet):
    order_by = filters.OrderingFilter(
        fields=(
            ("name", "name"),
            ("country", "country"),
        )
    )
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    country = filters.CharFilter(field_name="country", lookup_expr="icontains")

    class Meta:
        model = Exhibitor
        fields = ["name", "country"]
