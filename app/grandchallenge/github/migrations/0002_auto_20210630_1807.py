# Generated by Django 3.1.11 on 2021-06-30 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("github", "0001_initial")]

    operations = [
        migrations.RenameField(
            model_name="githubwebhookmessage",
            old_name="tarball",
            new_name="zipfile",
        )
    ]
