from rest_framework.routers import DefaultRouter

from .api.views import VisitViewSet, WhyVisitViewSet

app_name = "visit"
router = DefaultRouter()

router.register(r"plan-visit", VisitViewSet, basename="visit-list")
router.register(r"why-visit", WhyVisitViewSet, basename="why-visit-list")

urlpatterns = router.urls
