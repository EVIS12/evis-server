from rest_framework import mixins, viewsets
from rest_framework.response import Response

from evis.awards.api.serializers import StudentProjectSerializer
from evis.awards.models import StudentProject


class StudentProjectViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = StudentProject.objects.all()
    serializer_class = StudentProjectSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "Student Project Created Successfully"}, status=201)
