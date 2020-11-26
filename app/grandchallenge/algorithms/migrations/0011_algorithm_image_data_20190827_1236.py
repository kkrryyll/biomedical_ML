# Generated by Django 2.2.4 on 2019-08-27 12:36
from uuid import uuid4

from django.db import migrations


def create_algorithm_workstation(apps):
    Group = apps.get_model("auth", "Group")  # noqa: N806
    Workstation = apps.get_model("workstations", "Workstation")  # noqa: N806

    pk = uuid4()
    editors_group = Group.objects.create(
        name=f"workstations_workstation_{pk}_editors"
    )
    users_group = Group.objects.create(
        name=f"workstations_workstation_{pk}_users"
    )

    workstation = Workstation.objects.create(
        pk=pk,
        title="Algorithm Workstation",
        editors_group=editors_group,
        users_group=users_group,
    )

    return workstation


def algorithm_container_images_to_algorithms_forward(apps, schema_editor):
    # Forward, create Algorithm from AlgorithmImage

    Algorithm = apps.get_model("algorithms", "Algorithm")  # noqa: N806
    AlgorithmImage = apps.get_model(  # noqa: N806
        "algorithms", "AlgorithmImage"
    )
    Group = apps.get_model("auth", "Group")  # noqa: N806

    workstation = create_algorithm_workstation(apps)

    for ai in AlgorithmImage.objects.all():
        pk = uuid4()

        editors_group = Group.objects.create(
            name=f"algorithms_algorithm_{pk}_editors"
        )
        users_group = Group.objects.create(
            name=f"algorithms_algorithm_{pk}_users"
        )

        a = Algorithm.objects.create(
            pk=pk,
            description=ai.description,
            logo=ai.logo,
            slug=ai.slug,
            title=ai.title,
            editors_group=editors_group,
            users_group=users_group,
            workstation=workstation,
        )

        ai.algorithm_id = a.pk
        ai.save()

        if ai.creator:
            editors_group.user_set.add(ai.creator)


class Migration(migrations.Migration):
    dependencies = [("algorithms", "0010_auto_20190827_1159")]

    operations = [
        migrations.RunPython(
            algorithm_container_images_to_algorithms_forward, elidable=True,
        )
    ]
