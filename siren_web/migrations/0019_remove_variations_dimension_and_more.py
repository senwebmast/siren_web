# Generated by Django 5.0.1 on 2024-03-13 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "siren_web",
            "0018_variations_dimension_variations_idtechnologies_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="variations",
            name="dimension",
        ),
        migrations.RemoveField(
            model_name="variations",
            name="iterations",
        ),
        migrations.RemoveField(
            model_name="variations",
            name="startval",
        ),
        migrations.RemoveField(
            model_name="variations",
            name="step",
        ),
    ]