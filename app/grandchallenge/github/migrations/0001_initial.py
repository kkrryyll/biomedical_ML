# Generated by Django 3.1.11 on 2021-06-23 16:30

from django.db import migrations, models

import grandchallenge.core.storage
import grandchallenge.github.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GitHubWebhookMessage",
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
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="When we received the event.",
                    ),
                ),
                ("payload", models.JSONField(default=None, null=True)),
                (
                    "tarball",
                    models.FileField(
                        null=True,
                        storage=grandchallenge.core.storage.PrivateS3Storage(),
                        upload_to=grandchallenge.github.models.zipfile_path,
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="githubwebhookmessage",
            index=models.Index(
                fields=["created"], name="github_gith_created_66be85_idx"
            ),
        ),
    ]