# Generated by Django 4.2.5 on 2023-10-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("visit", "0004_registerinterest_alter_subscripenews_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="registerinterest",
            name="title",
            field=models.CharField(default="title", help_text="Enter a title", max_length=200),
            preserve_default=False,
        ),
    ]
