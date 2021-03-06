# Generated by Django 3.1.11 on 2021-06-01 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0011_auto_20190627_2132"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("challenges", "0005_auto_20210512_1437"),
    ]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="admins_group",
            field=models.OneToOneField(
                editable=False,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="admins_of_challenge",
                to="auth.group",
            ),
        ),
        migrations.AlterField(
            model_name="challenge",
            name="forum",
            field=models.OneToOneField(
                editable=False,
                on_delete=django.db.models.deletion.PROTECT,
                to="forum.forum",
            ),
        ),
        migrations.AlterField(
            model_name="challenge",
            name="participants_group",
            field=models.OneToOneField(
                editable=False,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="participants_of_challenge",
                to="auth.group",
            ),
        ),
    ]
