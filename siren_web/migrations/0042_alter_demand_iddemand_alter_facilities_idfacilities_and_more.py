# Generated by Django 5.0.1 on 2024-03-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "siren_web",
            "0041_alter_demand_iddemand_alter_facilities_idfacilities_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="demand",
            name="iddemand",
            field=models.AutoField(
                db_column="idDemand", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="facilities",
            name="idfacilities",
            field=models.AutoField(
                db_column="idfacilities", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="genetics",
            name="idgenetics",
            field=models.AutoField(
                db_column="idGenetics", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="optimisation",
            name="idoptimisation",
            field=models.AutoField(
                db_column="idOptimisation", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="settings",
            name="idsettings",
            field=models.AutoField(
                db_column="idSettings", primary_key=True, serialize=False
            ),
        ),
    ]