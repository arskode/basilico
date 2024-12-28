import enum
import typing as t


class NodeType(enum.Enum):
    ELEMENT = 1
    ATTRIBUTE = 2


class Node(t.Protocol):
    to_render: bool
    type: NodeType

    def render(self, w: t.TextIO) -> None: ...
    def string(self) -> str: ...
