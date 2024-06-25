import uuid

from django.db import models


class StudentProject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_status = models.CharField(max_length=100)
    team_number = models.IntegerField()
    university = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    team_come_with = models.CharField(max_length=100)
    project_abstract = models.TextField()

    def __str__(self):
        return self.project_name
