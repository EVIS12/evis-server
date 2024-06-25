import uuid

from django.db import models
from django.utils import timezone
from solo.models import SingletonModel


class BaseModel(SingletonModel):
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=timezone.now)

    class Meta:
        abstract = True


class TotalVisitor(BaseModel):
    pass


class AboutViews(BaseModel):
    pass


class RegistrationViews(BaseModel):
    pass


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
