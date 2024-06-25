from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from openpyxl import Workbook
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from evis.blog.models import Blog, News, Testimonials
from evis.conference.api.serializers import ContractFormSerializer
from evis.conference.models import AboutConferenceImage, ContractFile, ContractForm
from evis.dashboard.pagination import LargeResultsSetPagination, SmallResultsSetPagination
from evis.dashboard.serializers.advisors import (
    AdvisorsCreateSerializer,
    AdvisorsDetailSerializer,
    AdvisorsListSerializer,
    AdvisorsUpdateSerializer,
)
from evis.dashboard.serializers.blogs import (
    BlogDetailSerializer,
    BlogListSerializer,
    BlogUpdateSerializer,
    NewsCreateSerializer,
    NewsDetailSerializer,
    NewsListSerializer,
    NewsUpdateSerializer,
    TestimonialsCreateSerializer,
    TestimonialsDetailSerializer,
    TestimonialsListSerializer,
    TestimonialsUpdateSerializer,
)
from evis.dashboard.serializers.conference import (
    ConferenceImageCreateSerializer,
    ConferenceImageSerializer,
    ContractFileListSerializer,
    ContractFileSerializer,
)
from evis.dashboard.serializers.exhibitors import ExhibitorVersionSerializer
from evis.dashboard.serializers.speakers import (
    SpeakerListSerializer,
    SpeakerSerializer,
    SpeakersVersionListSerializer,
    SpeakersVersionSerializer,
)
from evis.exhibitor.api.serializers import (
    ExhibitorCreateSerializer,
    ExhibitorDetailSerializer,
    ExhibitorListSerializer,
    ExhibitorUpdateSerializer,
    OrganizersSerializer,
    ParticipantSerializer,
    WhyExhibitSerializer,
    WhyToAttendEvisSerializer,
)
from evis.exhibitor.filters import ExhibitorFilter
from evis.exhibitor.models import Exhibitor, ExhibitorVersion, Organizers, Participant, WhyExhibit, WhyToAttendEvis
from evis.home.api.serializers import ContactSerializer, LocationSerializer, StatisticSerializer, TimerSerializer
from evis.home.models import Contact, Location, Statistic, Timer
from evis.speakers.api.serializers import SpeakerDetailSerializer
from evis.speakers.filters import SpeakersFilter
from evis.speakers.models import Advisors, Speakers, SpeakersVersion
from evis.users.api.serializers import FloorPlanSerializer, RegisterLinkSerializer
from evis.users.models import FloorPlan, RegisterLink

from .filters import ContractFormFilter
from .permissions import IsAdmin


# Speakers
class SpeakersVersionViewSet(viewsets.ModelViewSet):
    queryset = SpeakersVersion.objects.all()
    serializer_class = SpeakersVersionSerializer
    permission_classes = [IsAdmin]

    def get_serializer_class(self):
        if self.action == "list":
            return SpeakersVersionListSerializer
        return SpeakersVersionSerializer


class SpeakersViewSet(viewsets.ModelViewSet):
    queryset = Speakers.objects.prefetch_related("version").all()
    serializer_class = SpeakerSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = SpeakersFilter
    permission_classes = [IsAdmin]

    def get_serializer_class(self):
        if self.action == "list":
            return SpeakerListSerializer
        elif self.action == "retrieve":
            return SpeakerDetailSerializer
        return SpeakerSerializer


# Exhibitors


class ExhibitorVersionViewSet(viewsets.ModelViewSet):
    queryset = ExhibitorVersion.objects.all()
    serializer_class = ExhibitorVersionSerializer
    permission_classes = [IsAdmin]


class ExhibitorViewSet(viewsets.ModelViewSet):
    queryset = Exhibitor.objects.prefetch_related("version").all()
    serializer_class = ExhibitorDetailSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = ExhibitorFilter
    permission_classes = [IsAdmin]
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return ExhibitorListSerializer
        elif self.action == "retrieve":
            return ExhibitorDetailSerializer
        elif self.action == "update" or self.action == "partial_update":
            return ExhibitorUpdateSerializer
        return ExhibitorCreateSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    pagination_class = SmallResultsSetPagination
    permission_classes = [IsAdmin]


class WhyExhibitViewSet(viewsets.ModelViewSet):
    queryset = WhyExhibit.objects.all()
    serializer_class = WhyExhibitSerializer
    permission_classes = [IsAdmin]


class WhyToAttendEvisViewSet(viewsets.ModelViewSet):
    queryset = WhyToAttendEvis.objects.all()
    serializer_class = WhyToAttendEvisSerializer
    permission_classes = [IsAdmin]


# Blogs


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = [IsAdmin]

    def get_serializer_class(self):
        if self.action == "list":
            return BlogListSerializer
        elif self.action == "update" or self.action == "partial_update":
            return BlogUpdateSerializer
        return BlogDetailSerializer


# News
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = [IsAdmin]

    def get_serializer_class(self):
        if self.action == "list":
            return NewsListSerializer
        elif self.action == "create":
            return NewsCreateSerializer
        elif self.action == "update" or self.action == "partial_update":
            return NewsUpdateSerializer
        return NewsDetailSerializer


# Testimonials


class TestimonialsViewSet(viewsets.ModelViewSet):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsDetailSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = [IsAdmin]

    def get_serializer_class(self):
        if self.action == "list":
            return TestimonialsListSerializer
        elif self.action == "create":
            return TestimonialsCreateSerializer
        elif self.action == "update":
            return TestimonialsUpdateSerializer
        return TestimonialsDetailSerializer


# Register Link


class RegisterLinkViewSet(viewsets.ModelViewSet):
    queryset = RegisterLink.objects.all()
    serializer_class = RegisterLinkSerializer
    permission_classes = [IsAdmin]


# Advisors Board


class AdvisorsViewSet(viewsets.ModelViewSet):
    queryset = Advisors.objects.all()
    serializer_class = AdvisorsDetailSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = [IsAdmin]

    def get_serializer_class(self):
        if self.action == "list":
            return AdvisorsListSerializer
        elif self.action == "create":
            return AdvisorsCreateSerializer
        elif self.action == "update":
            return AdvisorsUpdateSerializer
        return AdvisorsDetailSerializer


# Events


class TimerViewSet(viewsets.ViewSet):
    permission_classes = [IsAdmin]
    serializer_class = TimerSerializer
    queryset = Timer.objects.all()

    def retrieve(self, request, pk=None):
        timer = Timer.get_solo()
        serializer = TimerSerializer(timer)
        return Response(serializer.data)

    def list(self, request):
        timer = Timer.get_solo()
        serializer = TimerSerializer(timer)
        return Response(serializer.data)

    def update(self, request, pk=None):
        timer = Timer.get_solo()
        serializer = TimerSerializer(timer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        timer = Timer.get_solo()
        serializer = TimerSerializer(timer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Statistics


class StatisticViewSet(viewsets.ViewSet):
    serializer_class = StatisticSerializer
    permission_classes = [IsAdmin]
    queryset = Statistic.objects.all()

    def retrieve(self, request, pk=None):
        statistic = Statistic.get_solo()
        serializer = StatisticSerializer(statistic)
        return Response(serializer.data)

    def list(self, request):
        statistic = Statistic.get_solo()
        serializer = StatisticSerializer(statistic)
        return Response(serializer.data)

    def update(self, request, pk=None):
        statistic = Statistic.get_solo()
        serializer = StatisticSerializer(statistic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        statistic = Statistic.get_solo()
        serializer = StatisticSerializer(statistic, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Locations


class LocationViewSet(viewsets.ViewSet):
    serializer_class = LocationSerializer
    permission_classes = [IsAdmin]

    def retrieve(self, request, pk=None):
        location = Location.get_solo()
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def list(self, request):
        location = Location.get_solo()
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def update(self, request, pk=None):
        location = Location.get_solo()
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        location = Location.get_solo()
        serializer = LocationSerializer(location, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Conferences


class AboutConferenceImageViewSet(viewsets.ModelViewSet):
    queryset = AboutConferenceImage.objects.all()
    serializer_class = ConferenceImageSerializer
    permission_classes = [IsAdmin]

    # delete all images
    @action(detail=False, methods=["delete"])
    def delete_all(self, request):
        AboutConferenceImage.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if (
            self.action == "list"
            or self.action == "update"
            or self.action == "partial_update"
            or self.action == "retrieve"
        ):
            return ConferenceImageSerializer
        return ConferenceImageCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContractFileViewSet(viewsets.ModelViewSet):
    serializer_class = ContractFileListSerializer
    queryset = ContractFile.objects.all()
    permission_classes = [IsAdmin]

    def get_serializer_class(self):
        if self.action == "list":
            return ContractFileListSerializer
        return ContractFileSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# Contract Form


class ContractFormViewSet(viewsets.ModelViewSet):
    queryset = ContractForm.objects.all()
    serializer_class = ContractFormSerializer
    permission_classes = [IsAdmin]

    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContractFormFilter

    allowed_methods = ["list"]

    @action(detail=False, methods=["get"])
    def download_by_filter(self, request):
        """Download contract forms by filter

        Args:
            request (contract_file__type): (
                ("one", "One"),
                ("two", "Two"),
            )

        Returns:
            file: Download It as Excel File
        """
        contract_file_type = request.query_params.get("contract_file__type")

        if contract_file_type is None:
            contract_file_type = self.kwargs.get("contract_file__type")

        if contract_file_type is None or contract_file_type == "":
            return Response({"error": "add `contract_file__type` filter to URL"}, status=status.HTTP_400_BAD_REQUEST)

        contract_forms = self.queryset.filter(contract_file__type=contract_file_type)

        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = 'attachment; filename="contract_forms.xlsx"'

        wb = Workbook()
        ws = wb.active

        headers = ["Name", "Company", "Email", "Country", "Phone", "Industry", "Interested In"]

        ws.append(headers)

        for contract_form in contract_forms:
            data_row = [
                contract_form.name,
                contract_form.company,
                contract_form.email,
                contract_form.country,
                contract_form.phone,
                contract_form.industry,
                contract_form.interested_in,
            ]
            ws.append(data_row)

        wb.save(response)
        return response

    @action(detail=False, methods=["get"])
    def download_all_excel(self, request):
        contract_forms = self.queryset.all()
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = 'attachment; filename="contract_forms.xlsx"'

        wb = Workbook()
        ws = wb.active

        # Add headers
        headers = ["Name", "Company", "Email", "Country", "Phone", "Industry", "Interested In"]
        ws.append(headers)

        # Add data
        for contract_form in contract_forms:
            data_row = [
                contract_form.name,
                contract_form.company,
                contract_form.email,
                contract_form.country,
                contract_form.phone,
                contract_form.industry,
                contract_form.interested_in,
            ]
            ws.append(data_row)

        wb.save(response)
        return response

    @action(detail=True, methods=["get"])
    def download_excel(self, request, pk=None):
        contract_form = self.get_object()
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = f'attachment; filename="{contract_form.name}.xlsx"'

        wb = Workbook()
        ws = wb.active

        # Add headers
        headers = ["Name", "Company", "Email", "Country", "Phone", "Industry", "Interested In"]
        ws.append(headers)

        # Add data
        data_row = [
            contract_form.name,
            contract_form.company,
            contract_form.email,
            contract_form.country,
            contract_form.phone,
            contract_form.industry,
            contract_form.interested_in,
        ]
        ws.append(data_row)

        wb.save(response)
        return response


# Floor Plan


class FloorPlanViewSet(viewsets.ViewSet):
    serializer_class = FloorPlanSerializer
    queryset = FloorPlan.objects.all()
    permission_classes = [IsAdmin]

    def retrieve(self, request, pk=None):
        floor_plan = FloorPlan.get_solo()
        serializer = FloorPlanSerializer(floor_plan)
        return Response(serializer.data)

    def list(self, request):
        floor_plan = FloorPlan.get_solo()
        serializer = FloorPlanSerializer(floor_plan)
        return Response(serializer.data)

    def update(self, request, pk=None):
        floor_plan = FloorPlan.get_solo()
        serializer = FloorPlanSerializer(floor_plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        floor_plan = FloorPlan.get_solo()
        serializer = FloorPlanSerializer(floor_plan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Contact


class ContactViewSet(viewsets.ViewSet):
    serializer_class = ContactSerializer
    permission_classes = [IsAdmin]

    def retrieve(self, request, pk=None):
        contact = Contact.get_solo()
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def list(self, request):
        contact = Contact.get_solo()
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def update(self, request, pk=None):
        contact = Contact.get_solo()
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        contact = Contact.get_solo()
        serializer = ContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Organizers


class OrganizersViewSet(viewsets.ModelViewSet):
    queryset = Organizers.objects.all()
    serializer_class = OrganizersSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = [IsAdmin]
