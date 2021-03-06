# Generated by Django 3.1.1 on 2020-12-15 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("archives", "0002_auto_20201214_0939")]

    operations = [
        migrations.AlterModelOptions(
            name="archive",
            options={
                "ordering": ("created",),
                "permissions": [
                    (
                        "use_archive",
                        "Can use the objects in the archive as inputs to algorithms, reader studies and challenges.",
                    ),
                    ("upload_archive", "Can upload to archive"),
                ],
            },
        )
    ]
