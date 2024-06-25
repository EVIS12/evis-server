from rest_framework.pagination import PageNumberPagination


class BasePagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 5


class ParticipantPagination(BasePagination):
    pass


class ExhibitorVersionPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 5


class ExhibitorPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = "page_size"
    max_page_size = 5


class WhyExhibitPagination(BasePagination):
    pass


class WhyToAttendEvisPagination(BasePagination):
    pass


class OrganizersPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = "page_size"
    max_page_size = 5
