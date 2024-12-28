import pytest

from basilico import attributes as a
from basilico.elements import Element


@pytest.mark.parametrize(
    "node_name, node",
    [
        ("async", a.Async),
        ("autofocus", a.AutoFocus),
        ("autoplay", a.AutoPlay),
        ("checked", a.Checked),
        ("controls", a.Controls),
        ("defer", a.Defer),
        ("disabled", a.Disabled),
        ("loop", a.Loop),
        ("multiple", a.Multiple),
        ("muted", a.Muted),
        ("playsinline", a.PlaysInline),
        ("readonly", a.ReadOnly),
        ("required", a.Required),
        ("selected", a.Selected),
        ("popover", a.Popover),
    ],
)
def test_boolean_attributes(node_name, node):
    res = Element("div", node()).string()

    assert res == f"<div {node_name}></div>"


@pytest.mark.parametrize(
    "node_name, node",
    [
        ("accept", a.Accept),
        ("action", a.Action),
        ("alt", a.Alt),
        ("as", a.As),
        ("autocomplete", a.AutoComplete),
        ("charset", a.Charset),
        ("cite", a.CiteAttr),
        ("class", a.Class),
        ("cols", a.Cols),
        ("colspan", a.ColSpan),
        ("content", a.Content),
        ("crossorigin", a.CrossOrigin),
        ("datetime", a.DateTime),
        ("draggable", a.Draggable),
        ("enctype", a.EncType),
        ("dir", a.Dir),
        ("for", a.For),
        ("form", a.FormAttr),
        ("height", a.Height),
        ("hidden", a.Hidden),
        ("href", a.Href),
        ("id", a.ID),
        ("integrity", a.Integrity),
        ("label", a.LabelAttr),
        ("lang", a.Lang),
        ("list", a.List),
        ("loading", a.Loading),
        ("max", a.Max),
        ("maxlength", a.MaxLength),
        ("method", a.Method),
        ("min", a.Min),
        ("minlength", a.MinLength),
        ("name", a.Name),
        ("pattern", a.Pattern),
        ("placeholder", a.Placeholder),
        ("popovertarget", a.PopoverTarget),
        ("popovertargetaction", a.PopoverTargetAction),
        ("poster", a.Poster),
        ("preload", a.Preload),
        ("rel", a.Rel),
        ("role", a.Role),
        ("rows", a.Rows),
        ("rowspan", a.RowSpan),
        ("slot", a.SlotAttr),
        ("src", a.Src),
        ("srcset", a.SrcSet),
        ("step", a.Step),
        ("style", a.StyleAttr),
        ("tabindex", a.TabIndex),
        ("target", a.Target),
        ("title", a.TitleAttr),
        ("type", a.Type),
        ("value", a.Value),
        ("width", a.Width),
        ("popover", a.Popover),
    ],
)
def test_attributes(node_name, node):
    res = Element("div", node("wow")).string()

    assert res == f'<div {node_name}="wow"></div>'


def test_aria():
    res = a.Aria("selected", "true").string()

    assert res == ' aria-selected="true"'


def test_data():
    res = a.DataAttr("id", "wow").string()

    assert res == ' data-id="wow"'
