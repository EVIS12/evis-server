from django.db import models
from solo.models import SingletonModel


class BaseModel(SingletonModel):
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class TotalVisitor(BaseModel):
    pass


class AboutViews(BaseModel):
    pass


class RegistrationViews(BaseModel):
    pass
