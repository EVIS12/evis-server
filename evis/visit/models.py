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


class SubscripeNews(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200, help_text="Enter a first name")
    last_name = models.CharField(max_length=200, help_text="Enter a last name")
    email = models.EmailField(max_length=200, help_text="Enter a email")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Subscripe News"
        verbose_name_plural = "Subscripe News"


class RegisterInterest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=200, help_text="Enter a email")
    name = models.CharField(max_length=200, help_text="Enter a name")
    job_title = models.CharField(max_length=200, help_text="Enter a job title")
    company_name = models.CharField(max_length=200, help_text="Enter a company name")
    address = models.CharField(max_length=200, help_text="Enter a address")
    city = models.CharField(max_length=200, help_text="Enter a city")
    country = models.CharField(max_length=200, help_text="Enter a country")
    phone_number = models.CharField(max_length=200, help_text="Enter a phone number")
    business_nature = models.CharField(max_length=200, help_text="Enter a business nature")
    interested_in = models.CharField(max_length=200, help_text="Enter a interested in")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Register Interest"
        verbose_name_plural = "Register Interest"
