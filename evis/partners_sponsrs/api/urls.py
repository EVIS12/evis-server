from rest_framework.routers import DefaultRouter

from evis.partners_sponsrs.api.views import CategoryViewSet, PartnerAndSponserViewSet, PartnerSponsersViewSet

router = DefaultRouter()
router.register(r"partners_sponsers", PartnerAndSponserViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"list", PartnerSponsersViewSet)
urlpatterns = router.urls
