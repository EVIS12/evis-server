# Generated by Django 4.2.5 on 2024-02-08 08:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_registerlink_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registerlink",
            name="type",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
