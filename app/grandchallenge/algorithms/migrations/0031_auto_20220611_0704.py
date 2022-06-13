# Generated by Django 3.2.13 on 2022-06-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("algorithms", "0030_algorithm_editor_notes"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="runtime_metrics",
            field=models.JSONField(default=dict, editable=False),
        ),
        migrations.AlterField(
            model_name="job",
            name="input_prefixes",
            field=models.JSONField(
                default=dict,
                editable=False,
                help_text="Map of the ComponentInterfaceValue id to the path prefix to use for this input, e.g. {'1': 'foo/bar/'} will place CIV 1 at /input/foo/bar/<relative_path>",
            ),
        ),
    ]
