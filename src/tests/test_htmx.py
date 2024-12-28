import pytest

from basilico import htmx as hx
from basilico.elements import Button, Element


@pytest.mark.parametrize(
    "node_name, node",
    [
        ("boost", hx.Boost),
        ("get", hx.Get),
        ("post", hx.Post),
        ("push-url", hx.PushURL),
        ("select", hx.Select),
        ("select-oob", hx.SelectOOB),
        ("swap", hx.Swap),
        ("swap-oob", hx.SwapOOB),
        ("target", hx.Target),
        ("trigger", hx.Trigger),
        ("vals", hx.Vals),
        ("confirm", hx.Confirm),
        ("delete", hx.Delete),
        ("disable", hx.Disable),
        ("disabled-elt", hx.DisabledElt),
        ("disinherit", hx.Disinherit),
        ("encoding", hx.Encoding),
        ("ext", hx.Ext),
        ("headers", hx.Headers),
        ("history", hx.History),
        ("history-elt", hx.HistoryElt),
        ("include", hx.Include),
        ("indicator", hx.Indicator),
        ("params", hx.Params),
        ("patch", hx.Patch),
        ("preserve", hx.Preserve),
        ("prompt", hx.Prompt),
        ("put", hx.Put),
        ("replace-url", hx.ReplaceURL),
        ("request", hx.Request),
        ("sync", hx.Sync),
        ("validate", hx.Validate),
    ],
)
def test_attrs(node_name, node):
    res = Element("div", node("wow")).string()

    assert res == f'<div hx-{node_name}="wow"></div>'


def test_get():
    res = Button(hx.Post("/clicked"), hx.Swap("outerHTML")).string()

    assert res == '<button hx-post="/clicked" hx-swap="outerHTML"></button>'


def test_on():
    res = Element("div", hx.On("click", "alert('wow')")).string()

    assert res == """<div hx-on:click="alert('wow')"></div>"""
