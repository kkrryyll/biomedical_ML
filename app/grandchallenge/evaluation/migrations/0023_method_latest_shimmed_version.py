# Generated by Django 3.2.13 on 2022-06-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0022_auto_20220510_0807"),
    ]

    operations = [
        migrations.AddField(
            model_name="method",
            name="latest_shimmed_version",
            field=models.CharField(default="", editable=False, max_length=8),
        ),
    ]
