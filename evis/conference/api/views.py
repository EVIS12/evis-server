from rest_framework import status, viewsets
from rest_framework.response import Response

from evis.conference.models import AboutConferenceImage, ContractFile, ContractForm

from .serializers import AboutConferenceImageSerializer, ContractFileSerializer, ContractFormSerializer


class AboutConferenceImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutConferenceImage.objects.all()
    serializer_class = AboutConferenceImageSerializer


class ContractViewSet(viewsets.ViewSet):
    queryset = ContractForm.objects.all()
    serializer_class = ContractFormSerializer

    def create(self, request, *args, **kwargs):
        serializer = ContractFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        link_of_contract = serializer.data["contract_file"]
        list_of_contracts = ContractFile.objects.filter(id__in=link_of_contract)

        # Get the complete URL of the file
        contract_file_url = request.build_absolute_uri(list_of_contracts[0].file.url)

        # filename = list_of_contracts[0].file.name.split("/")[-1]

        return Response(
            data=[
                {"id": contract.id, "file": contract_file_url, "type": contract.type} for contract in list_of_contracts
            ],
            status=status.HTTP_201_CREATED,
            # headers={"Content-Disposition": f"attachment; filename={filename}"},
        )


class ContractFileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContractFile.objects.all()
    serializer_class = ContractFileSerializer
