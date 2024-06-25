from rest_framework.routers import DefaultRouter

from evis.awards.api.views import StudentProjectViewSet

router = DefaultRouter()
router.register(r"student-project-info", StudentProjectViewSet, basename="student-project-info")


urlpatterns = router.urls
