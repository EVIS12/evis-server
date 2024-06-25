from django_filters import rest_framework as filters

from .models import Speakers


class SpeakersFilter(filters.FilterSet):
    order_by = filters.OrderingFilter(
        fields=(
            ("version__year", "version__year"),
            ("company", "company"),
            ("country", "country"),
        )
    )

    class Meta:
        model = Speakers
        fields = {
            "home_page": ["icontains"],
            "conference_page": ["icontains"],
            "version__year": ["exact"],
            "country": ["icontains"],
            "company": ["icontains"],
        }
