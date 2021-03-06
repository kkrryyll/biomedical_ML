# Generated by Django 3.1.1 on 2020-11-20 08:07
from django.contrib.auth import get_user_model
from django.db import migrations


def create_credits(apps, schema_editor):
    Credit = apps.get_model("credits", "Credit")  # noqa: N806

    for user in get_user_model().objects.all():
        Credit.objects.create(user_id=user.id)


class Migration(migrations.Migration):
    dependencies = [("credits", "0001_initial")]

    operations = [migrations.RunPython(create_credits, elidable=True)]
