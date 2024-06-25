import uuid

from django.db import models
from django.utils import timezone


class SpeakersVersion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="speakers_version_photos", blank=True)
    year = models.CharField(default=timezone.now().year, max_length=4)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Speakers Versions"


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to="speakers_photos", blank=True)
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=timezone.now)


class Speakers(BaseModel):
    home_page = models.BooleanField(default=False)
    conference_page = models.BooleanField(default=False)
    company = models.CharField(max_length=100, blank=True)
    version = models.ManyToManyField(SpeakersVersion, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Speakers"


class Advisors(BaseModel):
    company = models.CharField(max_length=100)
    home_page = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Advisors"
