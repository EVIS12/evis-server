from rest_framework.routers import DefaultRouter

from evis.conference.api.views import AboutConferenceImageViewSet, ContractFileViewSet, ContractViewSet

router = DefaultRouter()
router.register(r"contract-form", ContractViewSet, basename="contract-form")
router.register(r"contract-file", ContractFileViewSet, basename="contract-file")
router.register(r"about-conference-image", AboutConferenceImageViewSet, basename="about_conference_image")

urlpatterns = router.urls
