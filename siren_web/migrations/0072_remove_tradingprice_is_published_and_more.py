# Generated by Django 5.0.1 on 2024-10-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("siren_web", "0071_tradingprice"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tradingprice",
            name="is_published",
        ),
        migrations.AlterField(
            model_name="tradingprice",
            name="id",
            field=models.AutoField(
                db_column="idTechnologies", primary_key=True, serialize=False
            ),
        ),
    ]
