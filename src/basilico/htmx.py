from basilico.attributes import Attribute, RawAttribute


class Boost(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-boost", v)


class Get(Attribute):
    def __init__(self, url: str) -> None:
        super().__init__("hx-get", url)


class On(RawAttribute):
    def __init__(self, name: str, v: str) -> None:
        super().__init__("hx-on:" + name, v)


class Post(Attribute):
    def __init__(self, url: str) -> None:
        super().__init__("hx-post", url)


class PushURL(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-push-url", v)


class Select(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-select", v)


class SelectOOB(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-select-oob", v)


class Swap(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-swap", v)


class SwapOOB(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-swap-oob", v)


class Target(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-target", v)


class Trigger(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-trigger", v)


class Vals(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-vals", v)


class Confirm(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-confirm", v)


class Delete(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-delete", v)


class Disable(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-disable", v)


class DisabledElt(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-disabled-elt", v)


class Disinherit(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-disinherit", v)


class Encoding(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-encoding", v)


class Ext(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-ext", v)


class Headers(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-headers", v)


class History(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-history", v)


class HistoryElt(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-history-elt", v)


class Include(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-include", v)


class Indicator(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-indicator", v)


class Params(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-params", v)


class Patch(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-patch", v)


class Preserve(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-preserve", v)


class Prompt(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-prompt", v)


class Put(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-put", v)


class ReplaceURL(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-replace-url", v)


class Request(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-request", v)


class Sync(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-sync", v)


class Validate(Attribute):
    def __init__(self, v: str) -> None:
        super().__init__("hx-validate", v)
