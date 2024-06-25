from rest_framework.routers import DefaultRouter

from evis.home.api.views import ContactViewSet, StatisticViewSet, TimerViewSet

router = DefaultRouter()
router.register(r"timer", TimerViewSet, basename="timer")
router.register(r"statistics", StatisticViewSet, basename="statistics")
router.register(r"contacts", ContactViewSet, basename="contacts")

urlpatterns = router.urls
