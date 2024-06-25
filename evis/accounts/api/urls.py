from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, activate_account, reset_password_confirm

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

# Define a common prefix
api_prefix = "api/v1/"

urlpatterns = [
    path(f"{api_prefix}activate-account/<str:uid>/<str:token>/", activate_account, name="activate-account"),
    path(f"{api_prefix}password-reset-account/<str:uid>/<str:token>/", reset_password_confirm, name="reset-password"),
]

urlpatterns += [
    path(f"{api_prefix}", include(router.urls)),
]
