from rest_framework.routers import DefaultRouter

from evis.attendees.api.views import AttendeesViewSet

router = DefaultRouter()
router.register(r"previous_attendees", AttendeesViewSet)
urlpatterns = router.urls
