# Generated by Django 3.2.12 on 2022-03-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reader_studies", "0018_auto_20220218_1221"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="displayset",
            options={"ordering": ("order", "created")},
        ),
        migrations.AddField(
            model_name="displayset",
            name="order",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
