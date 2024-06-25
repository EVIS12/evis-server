from rest_framework.routers import DefaultRouter

from evis.partners_sponsrs.api.views import PartnerAndSponserViewSet

router = DefaultRouter()
router.register(r"", PartnerAndSponserViewSet)
urlpatterns = router.urls
