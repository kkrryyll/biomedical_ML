# Generated by Django 3.2.13 on 2022-05-10 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reader_studies", "0026_auto_20220504_1424"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="images",
        ),
        migrations.RemoveField(
            model_name="readerstudy",
            name="hanging_list",
        ),
        migrations.RemoveField(
            model_name="readerstudy",
            name="images",
        ),
        migrations.RemoveField(
            model_name="readerstudy",
            name="use_display_sets",
        ),
        migrations.RemoveField(
            model_name="readerstudy",
            name="validate_hanging_list",
        ),
    ]
