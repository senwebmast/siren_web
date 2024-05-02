# Generated by Django 5.0.1 on 2024-05-02 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0063_rename_optimisation_optimisations_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="technologies",
            name="approach",
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name="technologies",
            name="capacity_step",
            field=models.FloatField(null=True),
        ),
    ]
