import pytest

from tests.documentation_tests.factories import DocPageFactory


@pytest.mark.django_db
def test_last_added_page_last_in_order():
    p1 = DocPageFactory()
    p2 = DocPageFactory()

    assert [p1.order, p2.order] == [1, 2]


@pytest.mark.django_db
@pytest.mark.parametrize(
    "move_op,expected",
    [(1, [2, 1, 3, 4]), (3, [1, 3, 2, 4]), (4, [1, 4, 2, 3])],
)
def test_page_move(move_op, expected):
    p1, p2, p3, p4 = (
        DocPageFactory(),
        DocPageFactory(),
        DocPageFactory(),
        DocPageFactory(),
    )

    assert [p1.order, p2.order, p3.order, p4.order] == [1, 2, 3, 4]

    # move second page
    p2.position(move_op)

    for p in [p1, p2, p3, p4]:
        p.refresh_from_db()

    assert [p.order for p in [p1, p2, p3, p4]] == expected


@pytest.mark.django_db
def test_child_page_position_on_save():
    p1 = DocPageFactory(parent=None)
    p2 = DocPageFactory(parent=None)
    assert [p1.order, p2.order] == [1, 2]

    # add a child to p1
    p1a = DocPageFactory(parent=p1)
    assert p1a.order == 2
    p2.refresh_from_db()
    assert p2.order == 3

    # add a child to p1a
    p1a_sub = DocPageFactory(parent=p1a)
    assert p1a_sub.order == 3
    p2.refresh_from_db()
    assert p2.order == 4

    # add another toplevel page
    p3 = DocPageFactory()
    assert [p1.order, p1a.order, p1a_sub.order, p2.order, p3.order] == [
        1,
        2,
        3,
        4,
        5,
    ]


@pytest.mark.django_db
def test_properties():
    p1 = DocPageFactory(parent=None)
    p2 = DocPageFactory(parent=None)
    p2a = DocPageFactory(parent=p2)
    p2b = DocPageFactory(parent=p2)
    p3 = DocPageFactory(parent=None)
    p3a = DocPageFactory(parent=p3)

    pages = [p1, p2, p2a, p2b, p3, p3a]
    counter = 0

    for p in pages[:-1]:
        counter += 1
        assert p.next == pages[counter]
    assert not p3a.next

    counter = len(pages) - 1
    for p in pages[:0:-1]:
        counter -= 1
        assert p.previous == pages[counter]
    assert not p1.previous

    assert not p1.children.all()
    assert p2a in p2.children.all()
    assert p2b in p2.children.all()
    assert p3a in p3.children.all()

    assert not p1.parent
    assert not p2.parent
    assert [p2a.parent, p2b.parent] == [p2, p2]
    assert p3a.parent == p3
