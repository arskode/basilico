from basilico.attributes import Attribute, RawAttribute


class Data(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-data", v)


class Init(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-init", v)


class Show(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-show", v)


class Bind(Attribute):
    def __init__(self, on_attr: str, v: str) -> None:
        super().__init__("x-bind:" + on_attr, v)


class On(Attribute):
    def __init__(self, event: str, v: str) -> None:
        super().__init__("x-on:" + event, v)


class Text(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-text", v)


class Html(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-html", v)


class Model(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-model", v)


class Modelable(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-modelable", v)


class For(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-for", v)


class Effect(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-effect", v)


class Ignore(Attribute):
    def __init__(self) -> None:
        super().__init__("x-ignore")


class Ref(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-ref", v)


class Cloak(Attribute):
    def __init__(self) -> None:
        super().__init__("x-cloak")


class Teleport(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-teleport", v)


class If(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-if", v)


class Id(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-id", v)


class Mask(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-mask", v)


class MaskDynamic(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("x-mask:dynamic", v)


class Class(RawAttribute):
    def __init__(self, v: str) -> None:
        super().__init__(":class", v)


class Transition(Attribute):
    """
    Transition allows you to create smooth transitions between when an element is shown or hidden.
    see https://alpinejs.dev/directives/transition
    """

    def __init__(self, v1: str = "", v2: str = "") -> None:
        super().__init__("x-transition" + v1, v2)
