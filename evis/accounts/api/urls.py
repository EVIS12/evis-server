from django.urls import path
from rest_framework import routers

from .views import UserViewSet, activate_account, reset_password_confirm

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("activate-account/<str:uid>/<str:token>/", activate_account, name="activate-account"),
    path("password-reset-account/<str:uid>/<str:token>/", reset_password_confirm, name="reset-password"),
]

urlpatterns += router.urls
