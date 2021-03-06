# Generated by Django 3.0.2 on 2020-02-18 10:33
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("products", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="modified",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="product", name="diseases", field=models.TextField()
        ),
        migrations.AlterField(
            model_name="product", name="key_features", field=models.TextField()
        ),
        migrations.AlterField(
            model_name="product",
            name="modified",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="product", name="population", field=models.TextField()
        ),
    ]
