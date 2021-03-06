# Generated by Django 3.1.11 on 2021-07-04 15:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("github", "0002_auto_20210630_1807"),
    ]

    operations = [
        migrations.CreateModel(
            name="GitHubUserToken",
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
                ("access_token", models.CharField(max_length=64)),
                ("access_token_expires", models.DateTimeField()),
                ("refresh_token", models.CharField(max_length=128)),
                ("refresh_token_expires", models.DateTimeField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        )
    ]
