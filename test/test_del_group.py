from model.group import Group


def test_del_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create_group(Group(name="test_group", header="HHH", footer="FFFF"))
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
