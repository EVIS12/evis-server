import datetime

from django.db import models
from solo.models import SingletonModel


class Timer(SingletonModel):
    time = models.CharField(default=datetime.timedelta(minutes=30))

    def __str__(self):
        return "Timer"

    class Meta:
        verbose_name_plural = "Timer"


class Statistic(SingletonModel):
    delegates = models.CharField(default=0)
    speakers = models.CharField(default=0)
    square_meters = models.CharField(default=0)
    exhibitors = models.CharField(default=0)
    country = models.CharField(default=0)

    def __str__(self):
        return "Statistic"

    class Meta:
        verbose_name_plural = "Statistic"


class Contact(models.Model):
    contact_type = models.CharField(max_length=100)
    contact_value = models.CharField(max_length=200)

    def __str__(self):
        return self.contact_type

    class Meta:
        verbose_name_plural = "Contact"
        unique_together = ("contact_type", "contact_value")
