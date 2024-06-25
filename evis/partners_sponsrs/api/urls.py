from rest_framework.routers import DefaultRouter

from evis.partners_sponsrs.api.views import CategoryViewSet, PartnerAndSponserViewSet

router = DefaultRouter()
router.register(r"", PartnerAndSponserViewSet)
router.register(r"categories", CategoryViewSet)
urlpatterns = router.urls
