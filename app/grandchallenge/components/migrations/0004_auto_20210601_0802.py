# Generated by Django 3.1.11 on 2021-06-01 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cases", "0003_auto_20210406_0753"),
        ("components", "0003_auto_20210323_1452"),
    ]

    operations = [
        migrations.AlterField(
            model_name="componentinterfacevalue",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="cases.image",
            ),
        ),
        migrations.AlterField(
            model_name="componentinterfacevalue",
            name="interface",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="components.componentinterface",
            ),
        ),
    ]
