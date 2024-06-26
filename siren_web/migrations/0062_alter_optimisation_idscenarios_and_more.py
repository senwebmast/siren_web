# Generated by Django 5.0.1 on 2024-04-26 03:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "siren_web",
            "0061_optimisation_idscenarios_optimisation_idtechnologies_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="optimisation",
            name="idscenarios",
            field=models.ForeignKey(
                db_column="idScenarios",
                on_delete=django.db.models.deletion.CASCADE,
                to="siren_web.scenarios",
            ),
        ),
        migrations.AlterField(
            model_name="optimisation",
            name="idtechnologies",
            field=models.ForeignKey(
                db_column="idTechnologies",
                on_delete=django.db.models.deletion.RESTRICT,
                to="siren_web.technologies",
            ),
        ),
    ]
