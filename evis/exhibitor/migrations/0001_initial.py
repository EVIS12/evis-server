# Generated by Django 4.2.4 on 2023-08-24 19:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExhibitorVersion",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("photo", models.ImageField(blank=True, upload_to="exhibitor_photos")),
                ("year", models.CharField(default=2023, max_length=4)),
            ],
            options={
                "verbose_name_plural": "Exhibitors Versions",
            },
        ),
        migrations.CreateModel(
            name="Organizers",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("logo", models.ImageField(upload_to="organizers_logo")),
            ],
            options={
                "verbose_name_plural": "Organizers",
            },
        ),
        migrations.CreateModel(
            name="Participant",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("logo", models.ImageField(upload_to="participant_logo")),
                ("type", models.CharField(choices=[("partner", "Partner"), ("sponsor", "Sponsor")], max_length=50)),
            ],
            options={
                "verbose_name_plural": "Participants",
            },
        ),
        migrations.CreateModel(
            name="WhyExhibit",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique ID for this item",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(help_text="Enter a title", max_length=200)),
                (
                    "description",
                    models.TextField(blank=True, help_text="Enter a brief description", max_length=1000, null=True),
                ),
                ("photo", models.ImageField(blank=True, null=True, upload_to="images/")),
            ],
            options={
                "verbose_name_plural": "Why Exhibit",
            },
        ),
        migrations.CreateModel(
            name="WhyToAttendEvis",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="Unique ID for this item",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(help_text="Enter a title", max_length=200)),
                (
                    "description",
                    models.TextField(blank=True, help_text="Enter a brief description", max_length=1000, null=True),
                ),
                ("photo", models.ImageField(blank=True, null=True, upload_to="images/")),
            ],
            options={
                "verbose_name": "Why to Attend EVIS",
                "verbose_name_plural": "Why to Attend EVIS",
            },
        ),
        migrations.CreateModel(
            name="Exhibitor",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("logo", models.ImageField(blank=True, upload_to="exhibitor_logos")),
                ("description", models.TextField()),
                ("standNumber", models.CharField(default=0, max_length=100)),
                ("website", models.URLField()),
                ("address", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("is_parter", models.BooleanField(default=False)),
                ("is_sponser", models.BooleanField(default=False)),
                ("facebook", models.URLField(blank=True)),
                ("twitter", models.URLField(blank=True)),
                ("instagram", models.URLField(blank=True)),
                ("version", models.ManyToManyField(blank=True, to="exhibitor.exhibitorversion")),
            ],
            options={
                "verbose_name_plural": "Exhibitors",
            },
        ),
    ]
