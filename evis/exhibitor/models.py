import uuid

from django.db import models

from evis.visit.models import BaseModel

PARTICIPANT_TYPE = (
    ("partner", "Partner"),
    ("sponsor", "Sponsor"),
)


class Participant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo = models.ImageField(upload_to="participant_logo")
    type = models.CharField(max_length=50, choices=PARTICIPANT_TYPE)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Participants"


class Exhibitor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="exhibitor_logos", blank=True)
    description = models.TextField()
    standNumber = models.CharField(max_length=100, default=0)
    website = models.URLField()
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    sponserShipTitle = models.CharField(max_length=50, blank=True)
    exhibitor_url = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Exhibitors"


class WhyExhibit(BaseModel):
    """Model representing why to exhibit"""

    class Meta:
        verbose_name_plural = "Why Exhibit"


class WhyToAttendEvis(BaseModel):
    """Model representing why to attend EVIS"""

    class Meta:
        verbose_name = "Why to Attend EVIS"
        verbose_name_plural = "Why to Attend EVIS"


class Organizers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo = models.ImageField(upload_to="organizers_logo")

    def __str__(self):
        return self.logo.name

    class Meta:
        verbose_name_plural = "Organizers"
