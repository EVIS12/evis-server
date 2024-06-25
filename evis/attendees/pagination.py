from rest_framework.pagination import PageNumberPagination


class AttendeesPagination(PageNumberPagination):
    page_size = 15
