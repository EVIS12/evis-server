from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from evis.blog.models import Blog
from evis.dashboard.analysis.serializers import (
    ActivityChartSerializer,
    RegisterLinkDetailSerializer,
    RegisterLinkListSerializer,
)
from evis.dashboard.models import ExhibitionViews, HomeViews, Region, RegistrationViews
from evis.dashboard.permissions import IsAdmin
from evis.users.models import RegisterLink

from .serializers import (
    BlogSerializer,
    ExhibitionViewsSerializer,
    HomeViewsSerializer,
    RegionCreateSerializer,
    RegionListSerializer,
    RegionSerializer,
    RegistrationViewsSerializer,
)


class RegionViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Region.objects.order_by("-registered_count")
    serializer_class = RegionSerializer

    def get_serializer(self, *args, **kwargs):
        if self.action == "create":
            return RegionCreateSerializer(*args, **kwargs)
        elif self.action == "list":
            return RegionListSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)


class TopBlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all().order_by("-view_count")
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]


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


class ExhibitionViewsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ExhibitionViews.objects.all()
    serializer_class = ExhibitionViewsSerializer
    # permission_classes = [IsAdmin]

    def get_serializer(self, *args, **kwargs):
        if self.action == "create":
            return ExhibitionViewsSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def list(self, request):
        exhibition_views = ExhibitionViews.get_solo()
        serializer = ExhibitionViewsSerializer(exhibition_views)
        return Response(serializer.data)


class RegistrationViewsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = RegistrationViews.objects.all()
    serializer_class = RegistrationViewsSerializer
    # permission_classes = [IsAdmin]

    def get_serializer(self, *args, **kwargs):
        if self.action == "create":
            return RegistrationViewsSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def list(self, request):
        registration_views = RegistrationViews.get_solo()
        serializer = RegistrationViewsSerializer(registration_views)
        return Response(serializer.data)


# set patch method to anonymous user also
class HomeViewsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = HomeViews.objects.all()
    serializer_class = HomeViewsSerializer
    # permission_classes = [IsAdmin]

    def get_serializer(self, *args, **kwargs):
        if self.action == "create":
            return HomeViewsSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def list(self, request):
        home_views = HomeViews.get_solo()
        serializer = HomeViewsSerializer(home_views)
        return Response(serializer.data)


class ActivityChartViewSet(viewsets.ViewSet):
    permission_classes = [IsAdmin]

    def list(self, request):
        total_visitor = HomeViews.get_solo()
        about_views = ExhibitionViews.get_solo()
        registration_views = RegistrationViews.get_solo()
        serializer = ActivityChartSerializer(
            {"total_visitor": total_visitor, "about_views": about_views, "registration_views": registration_views}
        )
        return Response(serializer.data)
