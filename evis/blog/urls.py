from rest_framework.routers import DefaultRouter

from .api.presscenter.views import BlogPressViewSet, NewsPressViewSet, TestimonialsPressViewSet
from .api.views import BlogHomePageViewSet, BlogViewSet, NewsViewSet, TestimonialsViewSet

app_name = "blog"
router = DefaultRouter()
router.register(r"blog", BlogViewSet, basename="blog")
router.register(r"blog-press", BlogPressViewSet, basename="blog-press")
router.register(r"blog-home", BlogHomePageViewSet, basename="blog-home")
router.register(r"news", NewsViewSet, basename="news")
router.register(r"news-press", NewsPressViewSet, basename="news-press")
router.register(r"testimonials", TestimonialsViewSet, basename="testimonials")
router.register(r"testimonials-press", TestimonialsPressViewSet, basename="testimonials-press")

urlpatterns = router.urls
