# Generated by Django 5.0.1 on 2024-10-25 07:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("siren_web", "0072_remove_tradingprice_is_published_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="tradingprice",
            table="tradingprice",
        ),
    ]
