from django_filters import rest_framework as filters

from evis.speakers.models import Advisors


class AdvisorsFilter(filters.FilterSet):
    class Meta:
        model = Advisors
        fields = {
            "home_page": ["exact"],
        }
