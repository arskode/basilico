import html
import io
import typing as t
from functools import lru_cache

from basilico.node import NodeType


def render_attr(w: t.TextIO, name: str, value: str | None = None) -> None:
    if value:
        w.write(kv_attr_str(name, value))
        return

    w.write(" " + name)


@lru_cache(maxsize=500)
def kv_attr_str(name: str, value: str) -> str:
    return f' {name}="{html.escape(value)}"'


class Attribute:
    type: NodeType = NodeType.ATTRIBUTE
    to_render: bool = True

    def __init__(self, name: str, value: str = "") -> None:
        self.name = name
        self.value = value

    def render(self, w: t.TextIO) -> None:
        if self.to_render:
            render_attr(w, self.name, self.value)

    def string(self) -> str:
        with io.StringIO() as w:
            self.render(w)
            return w.getvalue()


class RawAttribute(Attribute):
    """Attribute that doesn't escape its value."""

    def render(self, w: t.TextIO) -> None:
        if self.to_render:
            w.write(f' {self.name}="{self.value}"')


class Async(Attribute):
    def __init__(self) -> None:
        super().__init__("async")


class AutoFocus(Attribute):
    def __init__(self) -> None:
        super().__init__("autofocus")


class AutoPlay(Attribute):
    def __init__(self) -> None:
        super().__init__("autoplay")


class Checked(Attribute):
    def __init__(self) -> None:
        super().__init__("checked")


class Controls(Attribute):
    def __init__(self) -> None:
        super().__init__("controls")


class CrossOrigin(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("crossorigin", v)


class DateTime(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("datetime", v)


class Defer(Attribute):
    def __init__(self) -> None:
        super().__init__("defer")


class Disabled(Attribute):
    def __init__(self) -> None:
        super().__init__("disabled")


class Draggable(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("draggable", v)


class Loop(Attribute):
    def __init__(self) -> None:
        super().__init__("loop")


class Multiple(Attribute):
    def __init__(self) -> None:
        super().__init__("multiple")


class Muted(Attribute):
    def __init__(self) -> None:
        super().__init__("muted")


class PlaysInline(Attribute):
    def __init__(self) -> None:
        super().__init__("playsinline")


class ReadOnly(Attribute):
    def __init__(self) -> None:
        super().__init__("readonly")


class Required(Attribute):
    def __init__(self) -> None:
        super().__init__("required")


class Selected(Attribute):
    def __init__(self) -> None:
        super().__init__("selected")


class Accept(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("accept", v)


class Action(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("action", v)


class Alt(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("alt", v)


class Aria(Attribute):
    def __init__(self, name: str, v: str) -> None:
        super().__init__("aria-" + name, v)


class As(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("as", v)


class AutoComplete(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("autocomplete", v)


class Charset(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("charset", v)


class CiteAttr(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("cite", v)


class Class(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("class", v)


class Cols(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("cols", v)


class ColSpan(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("colspan", v)


class Content(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("content", v)


class SlotAttr(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("slot", v)


class DataAttr(Attribute):
    def __init__(self, name: str, v: str) -> None:
        super().__init__("data-" + name, v)


class For(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("for", v)


class FormAttr(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("form", v)


class Height(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("height", v)


class Hidden(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hidden", v)


class Href(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("href", v)


class ID(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("id", v)


class Integrity(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("integrity", v)


class LabelAttr(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("label", v)


class Lang(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("lang", v)


class List(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("list", v)


class Loading(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("loading", v)


class Max(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("max", v)


class MaxLength(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("maxlength", v)


class Method(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("method", v)


class Min(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("min", v)


class MinLength(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("minlength", v)


class Name(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("name", v)


class Pattern(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("pattern", v)


class Placeholder(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("placeholder", v)


class Popover(Attribute):
    """
    Can be used as a boolean attribute or as a key-value attribute
    """

    def __init__(self, v: str = "") -> None:
        super().__init__("popover", v)


class PopoverTarget(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("popovertarget", v)


class PopoverTargetAction(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("popovertargetaction", v)


class Poster(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("poster", v)


class Preload(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("preload", v)


class Rel(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("rel", v)


class Role(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("role", v)


class Rows(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("rows", v)


class RowSpan(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("rowspan", v)


class Src(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("src", v)


class SrcSet(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("srcset", v)


class Step(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("step", v)


class StyleAttr(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("style", v)


class TabIndex(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("tabindex", v)


class Target(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("target", v)


class TitleAttr(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("title", v)


class Type(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("type", v)


class Value(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("value", v)


class Width(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("width", v)


class EncType(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("enctype", v)


class Dir(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("dir", v)
