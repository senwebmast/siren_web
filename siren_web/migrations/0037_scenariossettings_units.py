# Generated by Django 5.0.1 on 2024-03-25 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0036_scenariossettings"),
    ]

    operations = [
        migrations.AddField(
            model_name="scenariossettings",
            name="units",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
