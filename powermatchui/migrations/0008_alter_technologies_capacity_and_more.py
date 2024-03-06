# Generated by Django 5.0.1 on 2024-03-03 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("powermatchui", "0007_technologies_lcoe_technologies_lcoe_cf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="technologies",
            name="capacity",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AlterField(
            model_name="technologies",
            name="capacity_max",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AlterField(
            model_name="technologies",
            name="capacity_min",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AlterField(
            model_name="technologies",
            name="capex",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AlterField(
            model_name="technologies",
            name="emissions",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=7, null=True
            ),
        ),
        migrations.AlterField(
            model_name="technologies",
            name="fom",
            field=models.DecimalField(
                blank=True, db_column="FOM", decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AlterField(
            model_name="technologies",
            name="initial",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=7, null=True
            ),
        ),
        migrations.AlterField(
            model_name="technologies",
            name="lcoe",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=7, null=True
            ),
        ),
        migrations.AlterField(
            model_name="technologies",
            name="lcoe_cf",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=7, null=True
            ),
        ),
        migrations.AlterField(
            model_name="technologies",
            name="mult",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="technologies",
            name="vom",
            field=models.DecimalField(
                blank=True, db_column="VOM", decimal_places=2, max_digits=7, null=True
            ),
        ),
    ]
