from rest_framework.routers import DefaultRouter

from evis.speakers.advisors.views import AdvisorsBoardViewSet, AdvisorsViewSet

router = DefaultRouter()
router.register(r"advisors", AdvisorsViewSet, basename="advisors")
router.register(r"advisors-board", AdvisorsBoardViewSet, basename="advisors-board")

urlpatterns = router.urls
