# Generated by Django 5.0.1 on 2024-03-24 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("siren_web", "0034_storageattributes_year"),
    ]

    operations = [
        migrations.RenameField(
            model_name="settings",
            old_name="context",
            new_name="sw_context",
        ),
    ]