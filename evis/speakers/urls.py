from rest_framework.routers import DefaultRouter

from evis.speakers.api.views import (
    ConferenceSpeakersViewSet,
    HomeSpeakersViewSet,
    SpeakersVersionViewSet,
    SpeakersViewSet,
)

router = DefaultRouter()
router.register(r"speakers", SpeakersViewSet, basename="speakers")
router.register(r"home-speakers", HomeSpeakersViewSet, basename="home-speakers")
router.register(r"conference-speakers", ConferenceSpeakersViewSet, basename="conference-speakers")
router.register(r"speaker-version", SpeakersVersionViewSet, basename="speaker-version")

urlpatterns = router.urls
