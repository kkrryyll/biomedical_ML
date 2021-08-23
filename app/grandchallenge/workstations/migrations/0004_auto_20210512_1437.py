# Generated by Django 3.1.9 on 2021-05-12 14:37

import stdimage.models
from django.db import migrations

import grandchallenge.core.storage


class Migration(migrations.Migration):
    dependencies = [
        ("workstations", "0003_auto_20210402_1508"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workstation",
            name="logo",
            field=stdimage.models.JPEGField(
                storage=grandchallenge.core.storage.PublicS3Storage(),
                upload_to=grandchallenge.core.storage.get_logo_path,
            ),
        ),
    ]