# Generated by Django 5.0.1 on 2025-05-21 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("siren_web", "0087_alter_demand_idscenarios_alter_demand_idtechnologies"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analysis",
            name="idscenarios",
            field=models.ForeignKey(
                blank=True,
                db_column="idScenarios",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="siren_web.scenarios",
            ),
        ),
        migrations.AlterField(
            model_name="scenariossettings",
            name="idscenarios",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="siren_web.scenarios"
            ),
        ),
    ]
