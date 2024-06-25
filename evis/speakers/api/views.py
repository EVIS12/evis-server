from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from evis.speakers.filters import SpeakersFilter
from evis.speakers.models import Speakers, SpeakersVersion
from evis.speakers.paginations import LargPagination

from .serializers import SpeakerDetailSerializer, SpeakerListSerializer, SpeakerVersionSerializer


class HomeSpeakersViewSet(viewsets.ReadOnlyModelViewSet):
    # pagination_class = SmallPagination
    filterset_class = SpeakersFilter

    def get_queryset(self):
        return Speakers.objects.filter(home_page=True)

    def get_serializer_class(self):
        return SpeakerListSerializer


class ConferenceSpeakersViewSet(viewsets.ReadOnlyModelViewSet):
    # pagination_class = SmallPagination
    filterset_class = SpeakersFilter

    def get_queryset(self):
        return Speakers.objects.filter(conference_page=True)

    def get_serializer_class(self):
        return SpeakerListSerializer


class SpeakersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Speakers.objects.all()
    serializer_class = SpeakerListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LargPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = SpeakersFilter
    search_fields = ["name", "job_title", "description", "company"]

    def get_serializer_class(self):
        if self.action == "list":
            return SpeakerListSerializer
        elif self.action == "retrieve":
            return SpeakerDetailSerializer
        return SpeakerListSerializer


# allow only list to speakersversion
class SpeakersVersionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SpeakersVersion.objects.all()
    serializer_class = SpeakerVersionSerializer
    # pagination_class = SmallPagination

    def get_serializer_class(self):
        if self.action == "list":
            return SpeakerVersionSerializer
        elif self.action == "retrieve":
            return SpeakerVersionSerializer
        return SpeakerVersionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.order_by("-year")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = {"results": serializer.data}
            return self.get_paginated_response(data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
