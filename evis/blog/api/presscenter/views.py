from rest_framework import viewsets
from rest_framework.response import Response

from evis.blog.api.serializers import (
    BlogDetailSerializer,
    BlogListSerializer,
    NewsDetailSerializer,
    NewsListSerializer,
    TestimonialsSerializer,
)
from evis.blog.models import Blog, News, Testimonials


class BlogPressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.filter(status=True, press_center=True)
    serializer_class = BlogListSerializer

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


class NewsPressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.filter(press_center=True)
    serializer_class = NewsListSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return NewsDetailSerializer
        return super().get_serializer_class()


class TestimonialsPressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonials.objects.filter(press_center=True)
    serializer_class = TestimonialsSerializer
