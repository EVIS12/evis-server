import uuid

from django.db import models


class Categorty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class PartnerAndSponser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ManyToManyField(Categorty, blank=True)
    logo = models.ImageField(upload_to="partners_sponsrs/")
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.logo.url

    class Meta:
        verbose_name = "Partner and Sponser"
        verbose_name_plural = "Partners and Sponsers"
