# Generated by Django 4.2.5 on 2023-10-30 19:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0006_alter_registrationviews_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="exhibitionviews",
            options={"verbose_name": "Exhibition View", "verbose_name_plural": "Exhibition Views"},
        ),
    ]
