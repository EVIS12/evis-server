from rest_framework.routers import DefaultRouter

from evis.attendees.api.views import CPDViewSet

router = DefaultRouter()
router.register(r"", CPDViewSet)
urlpatterns = router.urls
