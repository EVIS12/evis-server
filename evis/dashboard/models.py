import uuid

from django.db import models
from django.utils import timezone
from solo.models import SingletonModel


class BaseModel(SingletonModel):
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=timezone.now)

    class Meta:
        abstract = True


class HomeViews(BaseModel):
    class Meta:
        verbose_name = "Home View"
        verbose_name_plural = "Home Views"

    def increment_count(self, count):
        self.count += count
        self.save()


class ExhibitionViews(BaseModel):
    class Meta:
        verbose_name = "Exhibition View"
        verbose_name_plural = "Exhibition Views"

    def increment_count(self, count):
        self.count += count
        self.save()


class RegistrationViews(BaseModel):
    class Meta:
        verbose_name = "Registration View"
        verbose_name_plural = "Registration Views"

    def increment_count(self, count):
        self.count += count
        self.save()


class Mail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        unique=True,
        error_messages={"unique": "This email has already been used."},
    )
    created_at = models.DateTimeField(auto_now_add=timezone.now)

    class Meta:
        verbose_name = "Mail"
        verbose_name_plural = "Mails"
        ordering = ("-created_at",)

    def __str__(self):
        return self.email


class Region(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)  # Assuming country codes are 3 characters long
    registered_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.code}"

    def increment_registered_count(self):
        self.registered_count += 1
        self.save()
