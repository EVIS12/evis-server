from django_filters import rest_framework as filters

from evis.conference.models import ContractForm


class ContractFormFilter(filters.FilterSet):
    contract_file__type = filters.CharFilter(field_name="contract_file__type")

    class Meta:
        model = ContractForm
        fields = ["contract_file__type"]
