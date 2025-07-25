# Generated by Django 5.0.1 on 2025-06-04 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("siren_web", "0090_alter_facilities_facility_code_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="supplyfactors",
            name="idscenarios",
        ),
        migrations.RemoveField(
            model_name="supplyfactors",
            name="idtechnologies",
        ),
        migrations.RemoveField(
            model_name="supplyfactors",
            name="idzones",
        ),
        migrations.AddField(
            model_name="supplyfactors",
            name="idfacilities",
            field=models.ForeignKey(
                blank=True,
                db_column="idfacilities",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="siren_web.facilities",
            ),
        ),
    ]
