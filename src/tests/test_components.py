from basilico.attributes import ID, Class, Href, Rel
from basilico.components import HTML5, HTML5Props
from basilico.elements import Div, Link


def test_html5():
    res = HTML5(
        HTML5Props(
            title="wow",
            description="dude",
            language="en",
            head=[
                Link(Rel("stylesheet"), Href("/style.css")),
            ],
            body=[Div()],
        )
    ).string()

    assert (
        res
        == '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>wow</title><meta name="description" content="dude"><link rel="stylesheet" href="/style.css"></head><body><div></div></body></html>'  # noqa: E501
    )


def test_html5_only_title():
    res = HTML5(HTML5Props(title="wow")).string()

    assert (
        res
        == '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>wow</title></head><body></body></html>'  # noqa: E501
    )


def test_html5_html_attrs():
    res = HTML5(
        HTML5Props(
            title="wow",
            description="dude",
            language="en",
            head=[Link(Rel("stylesheet"), Href("/style.css"))],
            body=[Div()],
            html_attrs=[(Class("h-full")), ID("htmlid")],
        )
    ).string()

    assert (
        res
        == '<!doctype html><html lang="en" class="h-full" id="htmlid"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>wow</title><meta name="description" content="dude"><link rel="stylesheet" href="/style.css"></head><body><div></div></body></html>'  # noqa: E501
    )
