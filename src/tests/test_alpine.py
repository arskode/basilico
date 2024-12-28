import pytest

from basilico import alpine as x
from basilico.elements import Element


@pytest.mark.parametrize(
    "node_name, node",
    [
        ("data", x.Data),
        ("init", x.Init),
        ("show", x.Show),
        ("text", x.Text),
        ("html", x.Html),
        ("model", x.Model),
        ("modelable", x.Modelable),
        ("for", x.For),
        ("effect", x.Effect),
        ("ref", x.Ref),
        ("teleport", x.Teleport),
        ("if", x.If),
        ("id", x.Id),
        ("mask", x.Mask),
        ("mask:dynamic", x.MaskDynamic),
    ],
)
def test_attrs_with_string(node_name, node):
    res = Element("div", node("wow")).string()

    assert res == f'<div x-{node_name}="wow"></div>'


@pytest.mark.parametrize(
    "node_name, node",
    [
        ("cloak", x.Cloak),
        ("ignore", x.Ignore),
    ],
)
def test_attrs_with_no_args(node_name, node):
    res = Element("div", node()).string()

    assert res == f"<div x-{node_name}></div>"


@pytest.mark.parametrize(
    "node_name, node",
    [
        ("bind", x.Bind),
        ("on", x.On),
    ],
)
def test_attrs_with_attr_and_value(node_name, node):
    res = Element("div", node("wow", "dude")).string()

    assert res == f'<div x-{node_name}:wow="dude"></div>'


@pytest.mark.parametrize(
    "args, expected",
    [
        ([], "<div x-transition></div>"),
        ([""], "<div x-transition></div>"),
        ([".duration.500ms"], "<div x-transition.duration.500ms></div>"),
        (
            [":enter", "transition ease-out duration-300"],
            '<div x-transition:enter="transition ease-out duration-300"></div>',
        ),
    ],
)
def test_transition(args, expected):
    res = Element("div", x.Transition(*args)).string()

    assert res == expected


def test_class():
    res = Element("div", x.Class("open ? '' : 'hidden'")).string()

    assert res == """<div :class="open ? '' : 'hidden'"></div>"""
