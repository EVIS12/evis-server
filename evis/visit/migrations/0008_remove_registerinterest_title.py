# Generated by Django 4.2.5 on 2023-10-24 07:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("visit", "0007_remove_registerinterest_cell_phone"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="registerinterest",
            name="title",
        ),
    ]