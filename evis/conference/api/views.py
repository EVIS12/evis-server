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
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ContractFileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContractFile.objects.all()
    serializer_class = ContractFileSerializer
