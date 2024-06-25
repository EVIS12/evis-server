from rest_framework import viewsets
from rest_framework.response import Response

from evis.blog.models import Blog, News, Testimonials
from evis.blog.pagination import BigPagination

from .serializers import (
    BlogDetailSerializer,
    BlogListSerializer,
    NewsDetailSerializer,
    NewsListSerializer,
    TestimonialsSerializer,
)


class BlogHomePageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.filter(status=True, home_page=True)
    serializer_class = BlogListSerializer
    # pagination_class = BigPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BlogDetailSerializer
        return super().get_serializer_class()


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.filter(status=True)
    serializer_class = BlogListSerializer
    pagination_class = BigPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BlogDetailSerializer
        return super().get_serializer_class()


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    pagination_class = BigPagination

    def get_serializer_class(self):
        if self.action == "retrieve":
            return NewsDetailSerializer
        return super().get_serializer_class()


class TestimonialsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer
    pagination_class = BigPagination
