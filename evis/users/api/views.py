from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from evis.users.models import FloorPlan, RegisterLink

from .serializers import FloorPlanSerializer, RegisterLinkSerializer, UserSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class RegisterLinkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RegisterLinkSerializer
    queryset = RegisterLink.objects.all()


# Floor Plan ViewSet with solo


class FloorPlanViewSet(viewsets.ViewSet):
    def list(self, request):
        floor_plan = FloorPlan.get_solo()
        serializer = FloorPlanSerializer(floor_plan)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        floor_plan = FloorPlan.get_solo()
        serializer = FloorPlanSerializer(floor_plan)
        return Response(serializer.data)
