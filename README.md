# Basilico

Build HTML components in Python.

*Basilico* lets you create HTML components using pure Python code. Generate HTML5 markup effortlessly while building reusable components that enhance your development workflow.

## Key Features
- Write HTML components using familiar Python syntax
- Generate standards-compliant HTML5 output
- Create and maintain reusable components
- Keep your templates type-safe with Python's typing
- No external dependencies

# Usage
```shell
pip install basilico
```

```python
from basilico.attributes import Class, Href
from basilico.components import If
from basilico.elements import A, Li, Nav, Ol, Text
from basilico.node import Node


def navbar(logged_in: bool) -> Node:
    return Nav(
        Class("navbar"),
        Ol(
            navbar_item("Home", "/"),
            navbar_item("Contact", "/contact"),
            navbar_item("About", "/about"),
            If(
                logged_in is False,
                navbar_item("Login", "/login"),
            ),
        ),
    )


def navbar_item(name: str, path: str) -> Node:
    return Li(A(Href(path), Text(name)))
```

We can use generators to create components inline:
```python
from basilico.elements import Li, Text, Ul

items = ["Coffee", "Tea", "Milk"]
Ul(
    *(Li(Text(i)) for i in items),
)

# <ul>
#     <li>Coffee</li>
#     <li>Tea</li>
#     <li>Milk</li>
# </ul>
```

### HTMX support:
```python
from basilico import htmx as hx
from basilico.elements import Button

Button(hx.Get("/example"))

# <button hx-get="/example"></button>
```

### Alpine JS support:
```python
from basilico import alpine as x
from basilico.elements import Button, Div, Text

Div(
    x.Data("{ open: false }"),
    Button(x.On("click", "open = !open"), Text("Toggle")),
    Div(x.Show("open"), Text("Hello, Basilico!")),
)

# <div x-data="{ open: false }">
#     <button x-on:click="open = !open">Toggle</button>
#     <div x-show="open">Hello, Basilico!</div>
# </div>
```

## FastAPI example:
```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from basilico.attributes import Class, Src
from basilico.components import HTML5, HTML5Props
from basilico.elements import H1, Div, Script, Text
from basilico.node import Node

app = FastAPI()


def page(title: str, description: str, body: Node) -> Node:
    props = HTML5Props(
        title=title,
        description=description,
        language="en",
        head=[Script(Src("https://cdn.tailwindcss.com"))],
        body=[body],
    )
    return HTML5(props)


def body() -> Node:
    return Div(
        Class("min-h-screen flex items-center justify-center"),
        H1(
            Class("text-2xl font-bold text-teal-600 text-7xl"),
            Text("Hello, Basilico!"),
        ),
    )


@app.get("/")
def home():
    content = page(
        title="Home",
        description="This is a simple example of Basilico with FastAPI.",
        body=body(),
    )

    return HTMLResponse(content.string())
```
