# Generated by Django 4.2.4 on 2023-08-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutViews",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("count", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RegistrationViews",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("count", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TotalVisitor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("count", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
