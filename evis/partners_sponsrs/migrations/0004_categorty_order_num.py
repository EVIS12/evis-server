# Generated by Django 4.2.5 on 2024-03-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("partners_sponsrs", "0003_remove_partnerandsponser_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="categorty",
            name="order_num",
            field=models.IntegerField(default=0),
        ),
    ]
