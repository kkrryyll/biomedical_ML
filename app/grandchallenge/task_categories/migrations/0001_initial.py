# Generated by Django 3.1.1 on 2020-12-02 13:08

import django.contrib.postgres.fields.citext
from django.contrib.postgres.operations import CITextExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        CITextExtension(),
        migrations.CreateModel(
            name="TaskType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    django.contrib.postgres.fields.citext.CICharField(
                        max_length=16, unique=True
                    ),
                ),
            ],
            options={"ordering": ("type",)},
        ),
    ]
