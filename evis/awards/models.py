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
    team_leader_name = models.CharField(max_length=100, blank=True, null=True)
    team_leader_email = models.CharField(blank=True, null=True)
    team_leader_phone = models.CharField(max_length=100, blank=True, null=True)
    team_leader_social_media = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_name
