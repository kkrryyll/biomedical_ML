from grandchallenge.workstations.templatetags.workstations import (
    workstation_query,
)
from tests.algorithms_tests.factories import AlgorithmJobFactory
from tests.archives_tests.factories import ArchiveItemFactory
from tests.factories import ImageFactory, UserFactory, WorkstationConfigFactory
from tests.reader_studies_tests.factories import (
    DisplaySetFactory,
    ReaderStudyFactory,
)


def test_workstation_query_for_reader_studies(settings):
    reader_study = ReaderStudyFactory.build(
        workstation_config=WorkstationConfigFactory.build()
    )
    config = WorkstationConfigFactory.build()
    user = UserFactory.build()

    qs = workstation_query(reader_study=reader_study, user=user)
    assert "&" in qs
    assert (
        f"{settings.WORKSTATIONS_READY_STUDY_QUERY_PARAM}={reader_study.pk}"
        in qs
    )
    assert f"{settings.WORKSTATIONS_USER_QUERY_PARAM}={user.username}" in qs
    assert (
        f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={reader_study.workstation_config.pk}"
        in qs
    )

    qs = workstation_query(reader_study=reader_study)
    assert "&" in qs
    assert (
        f"{settings.WORKSTATIONS_READY_STUDY_QUERY_PARAM}={reader_study.pk}"
        in qs
    )
    assert (
        f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={reader_study.workstation_config.pk}"
        in qs
    )
    assert f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={config.pk}" not in qs

    qs = workstation_query(reader_study=reader_study, config=config)
    assert "&" in qs
    assert (
        f"{settings.WORKSTATIONS_READY_STUDY_QUERY_PARAM}={reader_study.pk}"
        in qs
    )
    assert (
        f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={reader_study.workstation_config.pk}"
        not in qs
    )
    assert f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={config.pk}" in qs

    reader_study.workstation_config = None

    qs = workstation_query(reader_study=reader_study)
    assert "&" not in qs
    assert (
        f"{settings.WORKSTATIONS_READY_STUDY_QUERY_PARAM}={reader_study.pk}"
        in qs
    )
    assert f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}" not in qs


def test_workstation_query_for_display_sets(settings):
    reader_study = ReaderStudyFactory.build(
        workstation_config=WorkstationConfigFactory.build()
    )
    config = WorkstationConfigFactory.build()
    display_set = DisplaySetFactory.build(reader_study=reader_study)

    qs = workstation_query(display_set=display_set)
    assert "&" in qs
    assert (
        f"{settings.WORKSTATIONS_DISPLAY_SET_QUERY_PARAM}={display_set.pk}"
        in qs
    )
    assert (
        f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={reader_study.workstation_config.pk}"
        in qs
    )
    assert f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={config.pk}" not in qs

    qs = workstation_query(display_set=display_set, config=config)
    assert "&" in qs
    assert (
        f"{settings.WORKSTATIONS_DISPLAY_SET_QUERY_PARAM}={display_set.pk}"
        in qs
    )
    assert (
        f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={reader_study.workstation_config.pk}"
        not in qs
    )
    assert f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={config.pk}" in qs

    reader_study.workstation_config = None

    qs = workstation_query(display_set=display_set)
    assert "&" not in qs
    assert (
        f"{settings.WORKSTATIONS_DISPLAY_SET_QUERY_PARAM}={display_set.pk}"
        in qs
    )
    assert f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}" not in qs


def test_workstation_query_for_archive_items(settings):
    config = WorkstationConfigFactory.build()
    archive_item = ArchiveItemFactory.build()

    qs = workstation_query(archive_item=archive_item, config=config)
    assert "&" in qs
    assert (
        f"{settings.WORKSTATIONS_ARCHIVE_ITEM_QUERY_PARAM}={archive_item.pk}"
        in qs
    )
    assert f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={config.pk}" in qs

    qs = workstation_query(archive_item=archive_item)
    assert "&" not in qs
    assert (
        f"{settings.WORKSTATIONS_ARCHIVE_ITEM_QUERY_PARAM}={archive_item.pk}"
        in qs
    )
    assert f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}" not in qs


def test_workstation_query_for_algorithms(settings):
    algorithm_job = AlgorithmJobFactory.build()
    config = WorkstationConfigFactory.build()

    qs = workstation_query(algorithm_job=algorithm_job)
    assert "&" not in qs
    assert (
        f"{settings.WORKSTATIONS_ALGORITHM_JOB_QUERY_PARAM}={algorithm_job.pk}"
        in qs
    )

    qs = workstation_query(algorithm_job=algorithm_job, config=config)
    assert "&" in qs
    assert (
        f"{settings.WORKSTATIONS_ALGORITHM_JOB_QUERY_PARAM}={algorithm_job.pk}"
        in qs
    )
    assert f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={config.pk}" in qs


def test_workstation_query_for_images(settings):
    image, overlay = ImageFactory.build_batch(2)
    config = WorkstationConfigFactory.build()

    qs = workstation_query(image=image)
    assert "&" not in qs
    assert f"{settings.WORKSTATIONS_BASE_IMAGE_QUERY_PARAM}={image.pk}" in qs
    assert (
        f"{settings.WORKSTATIONS_OVERLAY_QUERY_PARAM}={overlay.pk}" not in qs
    )
    assert f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={config.pk}" not in qs

    qs = workstation_query(image=image, overlay=overlay)
    assert "&" in qs
    assert f"{settings.WORKSTATIONS_BASE_IMAGE_QUERY_PARAM}={image.pk}" in qs
    assert f"{settings.WORKSTATIONS_OVERLAY_QUERY_PARAM}={overlay.pk}" in qs
    assert f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={config.pk}" not in qs

    qs = workstation_query(image=image, config=config)
    assert "&" in qs
    assert f"{settings.WORKSTATIONS_BASE_IMAGE_QUERY_PARAM}={image.pk}" in qs
    assert (
        f"{settings.WORKSTATIONS_OVERLAY_QUERY_PARAM}={overlay.pk}" not in qs
    )
    assert f"{settings.WORKSTATIONS_CONFIG_QUERY_PARAM}={config.pk}" in qs
