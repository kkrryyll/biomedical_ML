# Generated by Django 3.2.12 on 2022-03-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("verifications", "0002_auto_20201210_1040"),
    ]

    operations = [
        migrations.AlterField(
            model_name="verification",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
