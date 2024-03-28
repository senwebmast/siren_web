# Generated by Django 5.0.1 on 2024-03-28 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0043_analysis_idvariations_alter_analysis_idscenarios"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analysis",
            name="idvariations",
            field=models.ForeignKey(
                blank=True,
                db_column="idvariations",
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="siren_web.variations",
            ),
        ),
    ]
