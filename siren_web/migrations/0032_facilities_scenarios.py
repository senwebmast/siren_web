# Generated by Django 5.0.1 on 2024-03-19 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0031_scenariostechnologies_technologies_scenarios"),
    ]

    operations = [
        migrations.AddField(
            model_name="facilities",
            name="scenarios",
            field=models.ManyToManyField(
                blank=True,
                through="siren_web.ScenariosFacilities",
                to="siren_web.scenarios",
            ),
        ),
    ]
