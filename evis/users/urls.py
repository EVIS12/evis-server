from rest_framework.routers import DefaultRouter

from evis.users.api.views import FloorPlanViewSet, RegisterLinkViewSet

router = DefaultRouter()
router.register(r"register-links", RegisterLinkViewSet, basename="register-links")
router.register(r"floor-plan", FloorPlanViewSet, basename="floor-plan")

urlpatterns = router.urls
