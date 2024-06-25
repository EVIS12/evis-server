from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from evis.visit.models import RegisterInterest, SubscripeNews, Visit, WhyVisit

from .serializers import RegisterInterestSerializer, SubscripeNewsSerializer, VisitSerializer, WhyVisitSerializer


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


class SubscripeNewsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = SubscripeNews.objects.all()
    serializer_class = SubscripeNewsSerializer
    pagination_class = None


class RegisterInterestViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = RegisterInterest.objects.all()
    serializer_class = RegisterInterestSerializer
    pagination_class = None
