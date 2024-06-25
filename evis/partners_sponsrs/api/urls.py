from rest_framework.routers import DefaultRouter

from evis.partners_sponsrs.api.views import CategoryViewSet, PartnerAndSponserViewSet, PartnerSponsersViewSet

router = DefaultRouter()
router.register(r"partners_sponsers", PartnerAndSponserViewSet, basename="partners_sponsers")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"list", PartnerSponsersViewSet, basename="list")
urlpatterns = router.urls
