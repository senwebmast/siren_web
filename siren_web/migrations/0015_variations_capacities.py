# Generated by Django 5.0.1 on 2024-03-07 05:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0014_delete_stations"),
    ]

    operations = [
        migrations.CreateModel(
            name="variations",
            fields=[
                (
                    "idvariations",
                    models.AutoField(
                        db_column="idvariations", primary_key=True, serialize=False
                    ),
                ),
                (
                    "variation_name",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
                (
                    "variation_description",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
            ],
            options={
                "db_table": "variations",
            },
        ),
        migrations.CreateModel(
            name="capacities",
            fields=[
                ("idcapacities", models.AutoField(primary_key=True, serialize=False)),
                (
                    "capacity",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=9, null=True
                    ),
                ),
                (
                    "mult",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "capacity_max",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=9, null=True
                    ),
                ),
                (
                    "capacity_min",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=9, null=True
                    ),
                ),
                (
                    "idscenarios",
                    models.ForeignKey(
                        blank=True,
                        db_column="idScenarios",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="siren_web.scenarios",
                    ),
                ),
                (
                    "idtechnologies",
                    models.ForeignKey(
                        db_column="idTechnologies",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="siren_web.technologies",
                    ),
                ),
            ],
            options={
                "db_table": "capacities",
            },
        ),
    ]
