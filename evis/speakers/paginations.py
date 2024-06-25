from rest_framework.pagination import PageNumberPagination


class LargPagination(PageNumberPagination):
    page_size = 20
