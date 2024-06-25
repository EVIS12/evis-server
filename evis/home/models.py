import datetime

from django.db import models
from solo.models import SingletonModel


class Timer(SingletonModel):
    time = models.CharField(default=datetime.timedelta(minutes=30))

    def __str__(self):
        return "Timer"

    class Meta:
        verbose_name_plural = "Timer"


class Location(SingletonModel):
    location = models.URLField(default="https://www.google.com/maps/")

    def __str__(self):
        return "Location"

    class Meta:
        verbose_name_plural = "Location"


class Statistic(SingletonModel):
    delegates = models.CharField(default=0)
    speakers = models.CharField(default=0)
    vehicles = models.CharField(default=0)
    exhibitors = models.CharField(default=0)
    country = models.CharField(default=0)

    def __str__(self):
        return "Statistic"

    class Meta:
        verbose_name_plural = "Statistic"


class Contact(SingletonModel):
    email1 = models.EmailField(default="evis@nirvanaholding.com")
    email2 = models.EmailField(default="event@nirvanaholding.com", blank=True)
    phone1 = models.CharField(default="+55555 333 4444", max_length=20)
    phone2 = models.CharField(default="+55555 333 4444", max_length=20, blank=True)

    def __str__(self):
        return "Contact"

    class Meta:
        verbose_name_plural = "Contact"
