# Generated by Django 5.0.1 on 2024-04-01 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0050_alter_technologies_capacity_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="supplyfactors",
            name="col",
            field=models.PositiveIntegerField(blank=True, db_column="Col", null=True),
        ),
        migrations.AddField(
            model_name="supplyfactors",
            name="year",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="supplyfactors",
            name="idscenarios",
            field=models.ForeignKey(
                db_column="idScenarios",
                default=0,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="siren_web.scenarios",
            ),
            preserve_default=False,
        ),
    ]