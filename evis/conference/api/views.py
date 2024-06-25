import smtplib

from django.conf import settings
from django.core.mail import BadHeaderError
from rest_framework import status, viewsets
from rest_framework.response import Response
from templated_mail.mail import BaseEmailMessage

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
        try:
            BaseEmailMessage(
                template_name="emails/contract.html",
                context={
                    "name": serializer.data["name"],
                    "company": serializer.data["company"],
                    "email": serializer.data["email"],
                    "country": serializer.data["country"],
                    "phone": serializer.data["phone"],
                    "industry": serializer.data["industry"],
                    "contract_file": contract_file_url,
                },
            ).send(to=[settings.EMAIL_TO])
        except BadHeaderError:
            return Response({"message": "Invalid header found"}, status=status.HTTP_400_BAD_REQUEST)
        except smtplib.SMTPDataError:
            return Response({"message": "Invalid email address"}, status=status.HTTP_400_BAD_REQUEST)
        except OSError:
            return Response({"message": "Cannot assign requested address"}, status=status.HTTP_400_BAD_REQUEST)

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
