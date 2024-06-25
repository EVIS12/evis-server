from django.conf import settings
from django.core.mail import BadHeaderError
from rest_framework import mixins, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from templated_mail.mail import BaseEmailMessage

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                BaseEmailMessage(
                    template_name="emails/register.html",
                    context={
                        "name": serializer.data["name"],
                        "email": serializer.data["email"],
                        "job_title": serializer.data["job_title"],
                        "company_name": serializer.data["company_name"],
                        "address": serializer.data["address"],
                        "city": serializer.data["city"],
                        "country": serializer.data["country"],
                        "phone_number": serializer.data["phone_number"],
                        "business_nature": serializer.data["business_nature"],
                        "interested_in": serializer.data["interested_in"],
                    },
                ).send(to=[settings.EMAIL_TO])
            except BadHeaderError:
                return Response({"message": "Invalid header found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
