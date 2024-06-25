import uuid

from django.db import models


class BaseModel(models.Model):
    """Base model with common fields for Visit and WhyToAttendEvis"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Unique ID for this item")
    title = models.CharField(max_length=200, help_text="Enter a title")
    description = models.TextField(max_length=1000, help_text="Enter a brief description", blank=True, null=True)
    photo = models.ImageField(upload_to="images/", blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ["title"]

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Visit(BaseModel):
    """Model representing a visit to EVIS"""

    class Meta:
        verbose_name = "Visit"
        verbose_name_plural = "Visits"


class WhyVisit(BaseModel):
    """Model representing why to visit EVIS"""

    class Meta:
        verbose_name = "Why to visit"
        verbose_name_plural = "Why to visit"
