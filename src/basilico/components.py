import typing as t
from dataclasses import dataclass, field

from basilico.attributes import Charset, Content, Lang, Name
from basilico.elements import HTML, Body, Doctype, Head, Meta, Text, Title
from basilico.node import Node


def If(cond: bool, node: Node) -> Node:
    if not cond:
        node.to_render = False

    return node


@dataclass
class HTML5Props:
    title: str = ""
    description: str = ""
    language: str = ""
    head: t.Iterable[Node] = field(default_factory=list)
    body: t.Iterable[Node] = field(default_factory=list)
    html_attrs: t.Iterable[Node] = field(default_factory=list)


def HTML5(p: HTML5Props) -> Node:
    return Doctype(
        HTML(
            If(p.language != "", Lang(p.language)),
            *p.html_attrs,
            Head(
                Meta(Charset("utf-8")),
                Meta(Name("viewport"), Content("width=device-width, initial-scale=1")),
                Title(Text(p.title)),
                If(p.description != "", Meta(Name("description"), Content(p.description))),
                *p.head,
            ),
            Body(*p.body),
        ),
    )
