# Generated by Django 5.0.1 on 2024-03-05 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("powermatchui", "0011_alter_demand_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="analysis",
            name="component",
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name="analysis",
            name="heading",
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
