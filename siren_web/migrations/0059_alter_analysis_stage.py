# Generated by Django 5.0.1 on 2024-04-15 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0058_rename_iterations_variations_stages"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analysis",
            name="stage",
            field=models.IntegerField(blank=True, max_length=45, null=True),
        ),
    ]
