# Generated by Django 5.0.1 on 2024-03-25 05:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0039_alter_scenariossettings_idscenarios"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scenariossettings",
            name="idscenarios",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="siren_web.scenarios"
            ),
        ),
        migrations.AlterField(
            model_name="zones",
            name="idzones",
            field=models.PositiveIntegerField(
                db_column="idZones", primary_key=True, serialize=False
            ),
        ),
    ]