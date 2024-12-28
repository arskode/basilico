import html
import io
import typing as t

from basilico.node import Node, NodeType

VOID_ELEMENTS = (
    "area",
    "base",
    "br",
    "col",
    "command",
    "embed",
    "hr",
    "img",
    "input",
    "keygen",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
)


def render_elem_child(w: t.TextIO, child: Node, type_cond: NodeType) -> None:
    if child.type == type_cond:
        child.render(w)


def render_elem(w: t.TextIO, name: str, children: tuple[Node, ...]) -> None:
    w.write("<" + name)
    for c in children:
        render_elem_child(w, c, NodeType.ATTRIBUTE)
    w.write(">")

    if name in VOID_ELEMENTS:
        return

    for c in children:
        render_elem_child(w, c, NodeType.ELEMENT)

    w.write(f"</{name}>")


class Element:
    type: NodeType = NodeType.ELEMENT
    to_render: bool = True

    def __init__(self, name: str, *children: Node) -> None:
        self.name = name
        self.children = children

    def render(self, w: t.TextIO):
        if self.to_render:
            render_elem(w, self.name, self.children)

    def string(self) -> str:
        with io.StringIO() as w:
            self.render(w)
            return w.getvalue()


class Doctype(Element):
    def __init__(self, sibling: Node) -> None:
        self.sibling = sibling

    def render(self, w: t.TextIO) -> None:
        if self.to_render:
            w.write("<!doctype html>")
            self.sibling.render(w)


class Text(Element):
    def __init__(self, text: str) -> None:
        self.text = text

    def render(self, w: t.TextIO):
        if self.to_render:
            w.write(html.escape(self.text))


class Raw(Element):
    def __init__(self, text: str) -> None:
        self.text = text

    def render(self, w: t.TextIO):
        if self.to_render:
            w.write(self.text)


class A(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("a", *children)


class Address(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("address", *children)


class Area(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("area", *children)


class Article(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("article", *children)


class Aside(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("aside", *children)


class Audio(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("audio", *children)


class Base(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("base", *children)


class BlockQuote(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("blockquote", *children)


class Body(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("body", *children)


class Br(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("br", *children)


class Button(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("button", *children)


class Canvas(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("canvas", *children)


class Cite(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("cite", *children)


class Code(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("code", *children)


class Col(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("col", *children)


class ColGroup(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("colgroup", *children)


class Data(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("data", *children)


class DataList(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("datalist", *children)


class Details(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("details", *children)


class Dialog(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("dialog", *children)


class Div(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("div", *children)


class Dl(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("dl", *children)


class Embed(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("embed", *children)


class Form(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("form", *children)


class FieldSet(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("fieldset", *children)


class Figure(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("figure", *children)


class Footer(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("footer", *children)


class Head(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("head", *children)


class Header(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("header", *children)


class HGroup(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("hgroup", *children)


class Hr(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("hr", *children)


class HTML(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("html", *children)


class IFrame(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("iframe", *children)


class Img(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("img", *children)


class Input(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("input", *children)


class Label(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("label", *children)


class Legend(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("legend", *children)


class Li(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("li", *children)


class Link(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("link", *children)


class Main(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("main", *children)


class Menu(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("menu", *children)


class Meta(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("meta", *children)


class Meter(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("meter", *children)


class Nav(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("nav", *children)


class NoScript(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("noscript", *children)


class Object(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("object", *children)


class Ol(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("ol", *children)


class OptGroup(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("optgroup", *children)


class Option(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("option", *children)


class P(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("p", *children)


class Param(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("param", *children)


class Picture(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("picture", *children)


class Pre(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("pre", *children)


class Progress(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("progress", *children)


class Script(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("script", *children)


class Section(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("section", *children)


class Select(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("select", *children)


class Slot(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("slot", *children)


class Source(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("source", *children)


class Span(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("span", *children)


class Style(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("style", *children)


class Summary(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("summary", *children)


class SVG(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("svg", *children)


class Table(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("table", *children)


class TBody(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("tbody", *children)


class Td(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("td", *children)


class Template(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("template", *children)


class Textarea(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("textarea", *children)


class TFoot(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("tfoot", *children)


class Th(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("th", *children)


class THead(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("thead", *children)


class Tr(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("tr", *children)


class Ul(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("ul", *children)


class Wbr(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("wbr", *children)


class Abbr(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("abbr", *children)


class B(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("b", *children)


class Caption(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("caption", *children)


class Dd(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("dd", *children)


class Del(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("del", *children)


class Dfn(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("dfn", *children)


class Dt(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("dt", *children)


class Em(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("em", *children)


class FigCaption(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("figcaption", *children)


class H1(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("h1", *children)


class H2(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("h2", *children)


class H3(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("h3", *children)


class H4(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("h4", *children)


class H5(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("h5", *children)


class H6(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("h6", *children)


class I(Element):  # noqa: E742
    def __init__(self, *children: Node) -> None:
        super().__init__("i", *children)


class Ins(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("ins", *children)


class Kbd(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("kbd", *children)


class Mark(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("mark", *children)


class Q(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("q", *children)


class S(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("s", *children)


class Samp(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("samp", *children)


class Small(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("small", *children)


class Strong(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("strong", *children)


class Sub(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("sub", *children)


class Sup(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("sup", *children)


class Time(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("time", *children)


class Title(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("title", *children)


class U(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("u", *children)


class Var(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("var", *children)


class Video(Element):
    def __init__(self, *children: Node) -> None:
        super().__init__("video", *children)
