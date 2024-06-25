from rest_framework.routers import DefaultRouter

from evis.exhibitor.api.views import (
    ExhibitorSliderViewSet,
    ExhibitorVersionViewSet,
    ExhibitorViewSet,
    OrganizersViewSet,
    ParticipantViewSet,
    WhyExhibitViewSet,
    WhyToAttendEvisViewSet,
)

router = DefaultRouter()
router.register(r"participant", ParticipantViewSet, basename="participant")
router.register(r"exhibitors-version", ExhibitorVersionViewSet, basename="exhibitors")
router.register(r"why-exhibit", WhyExhibitViewSet, basename="why-exhibit")
router.register(r"why-to-attend-evis", WhyToAttendEvisViewSet, basename="why-to-attend-evis")
router.register(r"exhibitors", ExhibitorViewSet, basename="exhibitors")
router.register(r"exhibitors-slider", ExhibitorSliderViewSet, basename="exhibitors-slider")
router.register(r"organizers", OrganizersViewSet, basename="organizers")

urlpatterns = router.urls
