# Generated by Django 5.0.1 on 2024-04-01 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0048_demand_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="demand",
            name="year",
            field=models.PositiveIntegerField(),
        ),
    ]
