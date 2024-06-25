from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from evis.blog.models import Blog
from evis.dashboard.analysis.serializers import (
    ActivityChartSerializer,
    RegisterLinkDetailSerializer,
    RegisterLinkListSerializer,
)
from evis.dashboard.models import AboutViews, RegistrationViews, TotalVisitor
from evis.dashboard.pagination import LargeResultsSetPagination, SmallResultsSetPagination
from evis.dashboard.permissions import IsAdmin
from evis.users.models import RegisterLink

from .serializers import (
    AboutViewsDetailSerializer,
    AboutViewsSerializer,
    BlogSerializer,
    RegistrationViewsSerializer,
    TotalVisitorDetailSerializer,
    TotalVisitorSerializer,
)


class TopBlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all().order_by("-view_count")
    serializer_class = BlogSerializer
    pagination_class = SmallResultsSetPagination
    permission_classes = [IsAdmin]

    @action(detail=False, methods=["get"])
    def all(self, request):
        self.pagination_class = LargeResultsSetPagination
        return super().list(request)


class TopRegisterLinkViewSet(viewsets.ViewSet):
    permission_classes = [IsAdmin]

    def list(self, request):
        register_links = RegisterLink.objects.all().order_by("-rank")
        serializer = RegisterLinkListSerializer(register_links, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        register_link = RegisterLink.objects.get(pk=pk)
        serializer = RegisterLinkDetailSerializer(register_link)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        register_link = RegisterLink.objects.get(pk=pk)
        serializer = RegisterLinkDetailSerializer(register_link, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO: Add viewset for AboutViews, RegistrationViews, TotalVisitor (just list and update )
class AboutViewsViewSet(viewsets.ViewSet):
    permission_classes = [IsAdmin]

    def list(self, request):
        about_views = AboutViews.get_solo()
        serializer = AboutViewsSerializer(about_views)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        about_views = AboutViews.get_solo()
        serializer = AboutViewsDetailSerializer(about_views)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        about_views = AboutViews.get_solo()
        serializer = AboutViewsSerializer(about_views, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistrationViewsViewSet(viewsets.ViewSet):
    permission_classes = [IsAdmin]

    def list(self, request):
        registration_views = RegistrationViews.get_solo()
        serializer = RegistrationViewsSerializer(registration_views)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        registration_views = RegistrationViews.get_solo()
        serializer = RegistrationViewsSerializer(registration_views)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        registration_views = RegistrationViews.get_solo()
        serializer = RegistrationViewsSerializer(registration_views, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TotalVisitorViewSet(viewsets.ViewSet):
    permission_classes = [IsAdmin]

    def list(self, request):
        total_visitor = TotalVisitor.get_solo()
        serializer = TotalVisitorSerializer(total_visitor)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        total_visitor = TotalVisitor.get_solo()
        serializer = TotalVisitorDetailSerializer(total_visitor)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        total_visitor = TotalVisitor.get_solo()
        serializer = TotalVisitorSerializer(total_visitor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityChartViewSet(viewsets.ViewSet):
    permission_classes = [IsAdmin]

    def list(self, request):
        total_visitor = TotalVisitor.get_solo()
        about_views = AboutViews.get_solo()
        registration_views = RegistrationViews.get_solo()
        serializer = ActivityChartSerializer(
            {"total_visitor": total_visitor, "about_views": about_views, "registration_views": registration_views}
        )
        return Response(serializer.data)
