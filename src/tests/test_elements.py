import pytest

from basilico import elements as e
from basilico.attributes import Attribute
from basilico.components import If


def test_doctype():
    res = e.Doctype(e.Element("html")).string()

    assert res == "<!doctype html><html></html>"


@pytest.mark.parametrize(
    "node_name, node",
    [
        ("a", e.A),
        ("abbr", e.Abbr),
        ("address", e.Address),
        ("article", e.Article),
        ("aside", e.Aside),
        ("audio", e.Audio),
        ("b", e.B),
        ("blockquote", e.BlockQuote),
        ("body", e.Body),
        ("button", e.Button),
        ("canvas", e.Canvas),
        ("caption", e.Caption),
        ("cite", e.Cite),
        ("code", e.Code),
        ("colgroup", e.ColGroup),
        ("data", e.Data),
        ("datalist", e.DataList),
        ("dd", e.Dd),
        ("del", e.Del),
        ("details", e.Details),
        ("dfn", e.Dfn),
        ("dialog", e.Dialog),
        ("div", e.Div),
        ("dl", e.Dl),
        ("dt", e.Dt),
        ("em", e.Em),
        ("fieldset", e.FieldSet),
        ("figcaption", e.FigCaption),
        ("figure", e.Figure),
        ("footer", e.Footer),
        ("form", e.Form),
        ("h1", e.H1),
        ("h2", e.H2),
        ("h3", e.H3),
        ("h4", e.H4),
        ("h5", e.H5),
        ("h6", e.H6),
        ("head", e.Head),
        ("header", e.Header),
        ("hgroup", e.HGroup),
        ("html", e.HTML),
        ("i", e.I),
        ("iframe", e.IFrame),
        ("ins", e.Ins),
        ("kbd", e.Kbd),
        ("label", e.Label),
        ("legend", e.Legend),
        ("li", e.Li),
        ("main", e.Main),
        ("mark", e.Mark),
        ("menu", e.Menu),
        ("meter", e.Meter),
        ("nav", e.Nav),
        ("noscript", e.NoScript),
        ("object", e.Object),
        ("ol", e.Ol),
        ("optgroup", e.OptGroup),
        ("option", e.Option),
        ("p", e.P),
        ("picture", e.Picture),
        ("pre", e.Pre),
        ("progress", e.Progress),
        ("q", e.Q),
        ("s", e.S),
        ("samp", e.Samp),
        ("script", e.Script),
        ("section", e.Section),
        ("select", e.Select),
        ("slot", e.Slot),
        ("small", e.Small),
        ("span", e.Span),
        ("strong", e.Strong),
        ("style", e.Style),
        ("sub", e.Sub),
        ("summary", e.Summary),
        ("sup", e.Sup),
        ("svg", e.SVG),
        ("table", e.Table),
        ("tbody", e.TBody),
        ("td", e.Td),
        ("template", e.Template),
        ("textarea", e.Textarea),
        ("tfoot", e.TFoot),
        ("th", e.Th),
        ("thead", e.THead),
        ("time", e.Time),
        ("title", e.Title),
        ("tr", e.Tr),
        ("u", e.U),
        ("ul", e.Ul),
        ("var", e.Var),
        ("video", e.Video),
    ],
)
def test_elements(node_name, node):
    res = node(Attribute("wow", "dude")).string()

    assert res == f'<{node_name} wow="dude"></{node_name}>'


@pytest.mark.parametrize(
    "node_name, node",
    [
        ("area", e.Area),
        ("base", e.Base),
        ("br", e.Br),
        ("col", e.Col),
        ("embed", e.Embed),
        ("hr", e.Hr),
        ("img", e.Img),
        ("input", e.Input),
        ("link", e.Link),
        ("meta", e.Meta),
        ("param", e.Param),
        ("source", e.Source),
        ("wbr", e.Wbr),
    ],
)
def test_void_elements(node_name, node):
    res = node(Attribute("wow", "dude")).string()

    assert res == f'<{node_name} wow="dude">'


def test_text():
    res = e.Text("<div>").string()

    assert res == "&lt;div&gt;"


def test_raw():
    res = e.Raw("<div>").string()

    assert res == "<div>"


@pytest.mark.parametrize(
    "condition, expected",
    [
        (True, "<div><span></span></div>"),
        (False, "<div></div>"),
    ],
)
def test_if(condition, expected):
    res = e.Element("div", If(condition, e.Element("span"))).string()

    assert res == expected
