from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from evis.visit.models import Visit, WhyVisit

from .serializers import VisitSerializer, WhyVisitSerializer


class BasePagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 100


class BaseVisitViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = BasePagination

    def get_queryset(self):
        return self.queryset.all()


class VisitViewSet(BaseVisitViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class WhyVisitViewSet(BaseVisitViewSet):
    queryset = WhyVisit.objects.all()
    serializer_class = WhyVisitSerializer
