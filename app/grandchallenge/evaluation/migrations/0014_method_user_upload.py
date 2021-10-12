# Generated by Django 3.1.13 on 2021-10-08 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("uploads", "0003_delete_publicmedia"),
        ("evaluation", "0013_auto_20210922_1634"),
    ]

    operations = [
        migrations.AddField(
            model_name="method",
            name="user_upload",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="uploads.userupload",
            ),
        ),
    ]
