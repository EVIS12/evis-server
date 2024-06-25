from rest_framework.routers import DefaultRouter

from evis.visit.api.views import RegisterInterestViewSet

app_name = "register-interest"
router = DefaultRouter()

router.register(r"register-interest", RegisterInterestViewSet, basename="register-interest-list")

urlpatterns = router.urls
