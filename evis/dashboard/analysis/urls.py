from rest_framework.routers import DefaultRouter

from .views import (
    ActivityChartViewSet,
    ExhibitionViewsViewSet,
    HomeViewsViewSet,
    RegionViewSet,
    RegistrationViewsViewSet,
    TopBlogViewSet,
    TopRegisterLinkViewSet,
)

router = DefaultRouter()
router.register(r"activity-chart", ActivityChartViewSet, basename="activity-chart")
router.register(r"top-blog", TopBlogViewSet, basename="top-blog")
router.register(r"top-register-link", TopRegisterLinkViewSet, basename="top-register-link")
router.register(r"exhibition-views", ExhibitionViewsViewSet, basename="exhibition-views")
router.register(r"home-views", HomeViewsViewSet, basename="home-views")
router.register(r"registration-views", RegistrationViewsViewSet, basename="registration-views")
router.register(r"region", RegionViewSet, basename="region")
urlpatterns = router.urls
