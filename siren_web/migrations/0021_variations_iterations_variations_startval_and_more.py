# Generated by Django 5.0.1 on 2024-03-13 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0020_variations_dimension"),
    ]

    operations = [
        migrations.AddField(
            model_name="variations",
            name="iterations",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="variations",
            name="startval",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="variations",
            name="step",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=7, null=True
            ),
        ),
    ]
