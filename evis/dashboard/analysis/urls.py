from rest_framework.routers import DefaultRouter

from .views import (
    AboutViewsViewSet,
    ActivityChartViewSet,
    RegistrationViewsViewSet,
    TopBlogViewSet,
    TopRegisterLinkViewSet,
    TotalVisitorViewSet,
)

router = DefaultRouter()
router.register(r"activity-chart", ActivityChartViewSet, basename="activity-chart")
router.register(r"top-blog", TopBlogViewSet, basename="top-blog")
router.register(r"top-register-link", TopRegisterLinkViewSet, basename="top-register-link")
router.register(r"about-views", AboutViewsViewSet, basename="about-views")
router.register(r"total-visitor", TotalVisitorViewSet, basename="total-visitor")
router.register(r"registration-views", RegistrationViewsViewSet, basename="registration-views")

urlpatterns = router.urls
