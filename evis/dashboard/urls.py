from rest_framework.routers import DefaultRouter

from evis.dashboard.views import (
    AboutConferenceImageViewSet,
    AdvisorsViewSet,
    BlogViewSet,
    ContactViewSet,
    ContractFileViewSet,
    ContractFormViewSet,
    ExhibitorVersionViewSet,
    ExhibitorViewSet,
    FloorPlanViewSet,
    LocationViewSet,
    NewsViewSet,
    OrganizersViewSet,
    ParticipantViewSet,
    RegisterLinkViewSet,
    SpeakersVersionViewSet,
    SpeakersViewSet,
    StatisticViewSet,
    TestimonialsViewSet,
    TimerViewSet,
    WhyExhibitViewSet,
    WhyToAttendEvisViewSet,
)

router = DefaultRouter()
router.register(r"advisors", AdvisorsViewSet, basename="advisors-dashboard")
router.register(r"blog", BlogViewSet, basename="blog-dashboard")
router.register(r"conference-image", AboutConferenceImageViewSet, basename="conference-image-dashboard")
router.register(r"contract-file", ContractFileViewSet, basename="contract-file-dashboard")
router.register(r"contract-form", ContractFormViewSet, basename="contract-form-dashboard")
router.register(r"contact", ContactViewSet, basename="contact-dashboard")
router.register(r"exhibitors", ExhibitorViewSet, basename="exhibitors-dashboard")
router.register(r"exhibitor-version", ExhibitorVersionViewSet, basename="exhibitor-version-dashboard")
router.register(r"floor-plan", FloorPlanViewSet, basename="floor-plan-dashboard")
router.register(r"locations", LocationViewSet, basename="locations-dashboard")
router.register(r"news", NewsViewSet, basename="news-dashboard")
router.register(r"organizers", OrganizersViewSet, basename="organizers-dashboard")
router.register(r"participant", ParticipantViewSet, basename="participant-dashboard")
router.register(r"register-link", RegisterLinkViewSet, basename="register-link-dashboard")
router.register(r"speakers", SpeakersViewSet, basename="speakers-dashboard")
router.register(r"speaker-version", SpeakersVersionViewSet, basename="speaker-version-dashboard")
router.register(r"statistics", StatisticViewSet, basename="statistics-dashboard")
router.register(r"testimonials", TestimonialsViewSet, basename="testimonials-dashboard")
router.register(r"timer", TimerViewSet, basename="timer-dashboard")
router.register(r"why-exhibit", WhyExhibitViewSet, basename="why-exhibit-dashboard")
router.register(r"why-to-attend-evis", WhyToAttendEvisViewSet, basename="why-to-attend-evis-dashboard")
urlpatterns = router.urls
