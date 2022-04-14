# Generated by Django 3.2.10 on 2022-02-18 12:21
import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("components", "0008_alter_componentinterfacevalue_file"),
        ("reader_studies", "0017_auto_20220228_1443"),
    ]

    operations = [
        migrations.AddField(
            model_name="readerstudy",
            name="use_display_sets",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="DisplaySet",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "reader_study",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="display_sets",
                        to="reader_studies.readerstudy",
                    ),
                ),
                (
                    "values",
                    models.ManyToManyField(
                        blank=True,
                        related_name="display_sets",
                        to="components.ComponentInterfaceValue",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="answer",
            name="display_set",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="answers",
                to="reader_studies.displayset",
            ),
        ),
        migrations.AddField(
            model_name="historicalanswer",
            name="display_set",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="reader_studies.displayset",
            ),
        ),
    ]