# Generated by Django 5.0.1 on 2024-05-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0064_technologies_approach_technologies_capacity_step"),
    ]

    operations = [
        migrations.AddField(
            model_name="technologies",
            name="capacities",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]