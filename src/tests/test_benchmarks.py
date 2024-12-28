import io
import random

import pytest

from basilico.attributes import ID, Attribute, Class, Href, Rel
from basilico.components import HTML5, HTML5Props
from basilico.elements import Element, Li, Link, Ol, Text


@pytest.mark.benchmark(group="html")
def test_boolean_attributes(benchmark):
    a = Attribute("wow")

    def run():
        a.render(io.StringIO())

    benchmark(run)


@pytest.mark.benchmark(group="html")
def test_kv_attributes(benchmark):
    a = Attribute("wow", "dude")

    def run():
        a.render(io.StringIO())

    benchmark(run)


@pytest.mark.benchmark(group="html")
def test_element(benchmark):
    e = Element("div")

    def run():
        e.render(io.StringIO())

    benchmark(run)


@pytest.mark.benchmark(group="template")
def test_template(benchmark):
    items = [str(random.randint(0, 100)) for _ in range(100)]
    t = HTML5(
        HTML5Props(
            title="wow",
            description="dude",
            language="en",
            head=[Link(Rel("stylesheet"), Href("/style.css"))],
            body=[
                Ol(
                    *(Li(Text(i)) for i in items),
                )
            ],
            html_attrs=[(Class("h-full")), ID("htmlid")],
        )
    )

    def run():
        t.render(io.StringIO())

    benchmark(run)
