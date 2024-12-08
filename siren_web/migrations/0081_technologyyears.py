# Generated by Django 5.0.1 on 2024-12-08 02:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("siren_web", "0080_alter_capacities_idcapacities"),
    ]

    operations = [
        migrations.CreateModel(
            name="TechnologyYears",
            fields=[
                (
                    "idtechnologyyears",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("year", models.IntegerField(default=0, null=True)),
                ("capex", models.FloatField(null=True)),
                ("fom", models.FloatField(db_column="FOM", null=True)),
                ("vom", models.FloatField(db_column="VOM", null=True)),
                ("lifetime", models.FloatField(null=True)),
                ("discount_rate", models.FloatField(null=True)),
                ("capacity", models.FloatField(null=True)),
                ("capacity_factor", models.FloatField(null=True)),
                ("mult", models.FloatField(null=True)),
                ("approach", models.CharField(blank=True, max_length=45, null=True)),
                ("capacity_max", models.FloatField(null=True)),
                ("capacity_min", models.FloatField(null=True)),
                ("capacity_step", models.FloatField(null=True)),
                ("capacities", models.CharField(blank=True, max_length=50, null=True)),
                ("emissions", models.FloatField(null=True)),
                ("initial", models.FloatField(null=True)),
                ("lcoe", models.FloatField(null=True)),
                ("lcoe_cf", models.FloatField(null=True)),
                (
                    "idtechnologies",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="siren_web.technologies",
                    ),
                ),
            ],
            options={
                "db_table": "TechnologyYears",
            },
        ),
    ]