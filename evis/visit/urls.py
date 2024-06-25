from rest_framework.routers import DefaultRouter

from .api.views import SubscripeNewsViewSet, VisitViewSet, WhyVisitViewSet

app_name = "visit"
router = DefaultRouter()

router.register(r"plan-visit", VisitViewSet, basename="visit-list")
router.register(r"why-visit", WhyVisitViewSet, basename="why-visit-list")
router.register(r"subscripe-news", SubscripeNewsViewSet, basename="subscripe-news-list")

urlpatterns = router.urls
