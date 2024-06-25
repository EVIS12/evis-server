import uuid

from django.db import models

FILE_TYPES = (
    ("one", "One"),
    ("two", "Two"),
)


class AboutConferenceImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="about_conference_images/")

    class Meta:
        verbose_name_plural = "About Conference Images"


class ContractFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to="contract_files/")
    type = models.CharField(max_length=100, choices=FILE_TYPES)

    class Meta:
        verbose_name_plural = "Contract Files"


class ContractForm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    interested_in = models.CharField(max_length=100)
    contract_file = models.ManyToManyField(ContractFile)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contract Forms"
