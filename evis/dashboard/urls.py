from rest_framework.routers import DefaultRouter

from evis.dashboard.views import (
    AboutConferenceImageViewSet,
    AdvisorsViewSet,
    AttendeesViewSet,
    BlogViewSet,
    CategoryPartnerAndSponserViewSet,
    ContactViewSet,
    ContractFileTypeViewSet,
    ContractFileViewSet,
    ContractFormViewSet,
    CPDViewSet,
    ExhibitorViewSet,
    MailViewSet,
    NewsViewSet,
    OrganizersViewSet,
    ParticipantViewSet,
    PartnerAndSponserViewSet,
    RegisterInterestTitlesViewSet,
    RegisterInterestViewSet,
    RegisterLinkViewSet,
    SpeakersVersionViewSet,
    SpeakersViewSet,
    StatisticViewSet,
    StudentProjectViewSet,
    SubscripeNewsViewSet,
    TestimonialsViewSet,
    TimerViewSet,
    WhyExhibitViewSet,
    WhyToAttendEvisViewSet,
)

router = DefaultRouter()
router.register(r"advisors", AdvisorsViewSet, basename="advisors-dashboard")
router.register(r"attendees", AttendeesViewSet, basename="attendees-dashboard")
router.register(r"blog", BlogViewSet, basename="blog-dashboard")
router.register(
    r"category-partner-sponser", CategoryPartnerAndSponserViewSet, basename="category-partner-sponser-dashboard"
)
router.register(r"conference-image", AboutConferenceImageViewSet, basename="conference-image-dashboard")
router.register(r"contract-file", ContractFileViewSet, basename="contract-file-dashboard")
router.register(r"contract-file-types", ContractFileTypeViewSet, basename="contract-file-type-dashboard")
router.register(r"contract-form", ContractFormViewSet, basename="contract-form-dashboard")
router.register(r"cpd", CPDViewSet, basename="cpd-dashboard")
router.register(r"contact", ContactViewSet, basename="contact-dashboard")
router.register(r"exhibitors", ExhibitorViewSet, basename="exhibitors-dashboard")
router.register(r"mail", MailViewSet, basename="mail-dashboard")
router.register(r"news", NewsViewSet, basename="news-dashboard")
router.register(r"organizers", OrganizersViewSet, basename="organizers-dashboard")
router.register(r"participant", ParticipantViewSet, basename="participant-dashboard")
router.register(r"partners_sponsrs", PartnerAndSponserViewSet, basename="partner-and-sponser-dashboard")
router.register(r"register-link", RegisterLinkViewSet, basename="register-link-dashboard")
router.register(r"register-interest", RegisterInterestViewSet, basename="register-interest-dashboard")
router.register(
    r"register-interest-titles", RegisterInterestTitlesViewSet, basename="register-interest-titles-dashboard"
)
router.register(r"speakers", SpeakersViewSet, basename="speakers-dashboard")
router.register(r"speaker-version", SpeakersVersionViewSet, basename="speaker-version-dashboard")
router.register(r"statistics", StatisticViewSet, basename="statistics-dashboard")
router.register(r"student-project-info", StudentProjectViewSet, basename="student-project-info-dashboard")
router.register(r"subscripe-news", SubscripeNewsViewSet, basename="subscripe-news-dashboard")
router.register(r"testimonials", TestimonialsViewSet, basename="testimonials-dashboard")
router.register(r"timer", TimerViewSet, basename="timer-dashboard")
router.register(r"why-exhibit", WhyExhibitViewSet, basename="why-exhibit-dashboard")
router.register(r"why-to-attend-evis", WhyToAttendEvisViewSet, basename="why-to-attend-evis-dashboard")
urlpatterns = router.urls
