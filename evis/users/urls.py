from rest_framework.routers import DefaultRouter

from evis.users.api.views import RegisterLinkViewSet

router = DefaultRouter()
router.register(r"register-links", RegisterLinkViewSet, basename="register-links")

urlpatterns = router.urls
