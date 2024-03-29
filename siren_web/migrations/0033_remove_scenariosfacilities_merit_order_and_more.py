# Generated by Django 5.0.1 on 2024-03-19 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0032_facilities_scenarios"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="scenariosfacilities",
            name="merit_order",
        ),
        migrations.RemoveField(
            model_name="technologies",
            name="merit_order",
        ),
        migrations.AlterField(
            model_name="scenariosfacilities",
            name="idfacilities",
            field=models.ForeignKey(
                db_column="idfacilities",
                on_delete=django.db.models.deletion.RESTRICT,
                to="siren_web.facilities",
            ),
        ),
        migrations.AlterField(
            model_name="scenariosfacilities",
            name="idscenarios",
            field=models.ForeignKey(
                db_column="idScenarios",
                on_delete=django.db.models.deletion.RESTRICT,
                to="siren_web.scenarios",
            ),
        ),
        migrations.AlterField(
            model_name="scenariostechnologies",
            name="idscenarios",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="siren_web.scenarios"
            ),
        ),
        migrations.AlterField(
            model_name="scenariostechnologies",
            name="idtechnologies",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                to="siren_web.technologies",
            ),
        ),
    ]
