# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symb = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symb) for i in range(random.randrange(maxlen))])

test_data = [Group(name="", header="", footer="")] + [Group(name=random_string("name", 15),
                                                            header=random_string("header", 20),
                                                            footer=random_string("footer", 20)) for i in range(2)]

@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create_group(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


