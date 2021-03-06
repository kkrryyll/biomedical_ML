# Generated by Django 3.1.13 on 2021-10-05 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("workstation_configs", "0008_auto_20210920_1439")]

    operations = [
        migrations.AlterField(
            model_name="workstationconfig",
            name="auto_jump_center_of_gravity",
            field=models.BooleanField(
                default=True,
                help_text="Jump to center of gravity of first output when viewing algorithm results or the first overlay segment when viewing a reader study",
            ),
        )
    ]
