# Generated by Django 4.2.5 on 2023-10-23 12:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("visit", "0006_registerinterest_interested_in"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="registerinterest",
            name="cell_phone",
        ),
    ]
