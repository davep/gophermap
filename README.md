# gophermap - A simple library for parsing Gopher maps

`gophermap` is a small and simple library that provides code for parsing
Gopher responses.

## Installation

`gophermap` is [available from pypi](https://pypi.org/project/gophermap/)
and can be installed with your package installer of choice.

With `pip`:

```shell
pip install gophermap
```

With `uv`:

```shell
uv add gophermap
```

## Quick start

The library provides a single main parsing class called `GopherMap`. It is
initialised with a response from a Gopher server, and the `items` property
provides a list of `GopherItem` objects.

A very minimal parser might look like this:

```python
import fileinput
from gophermap import GopherMap

def parse_input() -> None:
    with fileinput.input() as gopher_map:
        for gopher_item in GopherMap("".join(gopher_map)).items:
            print(f"{gopher_item!r}")
```

The library contains a simple test command line tool, which can be accessed
either via the Python `-m` switch, or depending on your environment, via the
`gophermap` command. For example, given this content of a file called
`gophermap`:

```text
iSome places to find me and more of my stuff		null.host	1
i~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~		null.host	0
i		null.host	1
hFind me all over	URL:https://davep.at/	tilde.team	70
hFind me in Geminispace	URL:gemini://tilde.team/~davep/	tilde.team	70
hMy blog	URL:https://blog.davep.org/	tilde.team	70
hfinger://plan.cat/davep	URL:finger://plan.cat/davep	tilde.team	70
hfinger://tilde.team/davep	URL:finger://tilde.team/davep	tilde.team	70
i		null.host	1
iMy current projects		null.host	1
i~~~~~~~~~~~~~~~~~~~		null.host	0
i		null.host	1
h[Web] Rogallo - A Gemini/Gopher/Finger client for the terminal	URL:https://rogallo.davep.dev/	tilde.team	70
h[Gemini] Rogallo - A Gemini/Gopher/Finger client for the terminal	URL:gemini://tilde.team/~davep/rogallo/	tilde.team	70
.
```

The `gophermap` command (or `python -m gophermap`) would produce:

```sh
$ gophermap gophermap
GopherItem(type=<ItemType.INFO: 'i'>, display_text='Some places to find me and more of my stuff', selector='', host='null.host', port=1)
GopherItem(type=<ItemType.INFO: 'i'>, display_text='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', selector='', host='null.host', port=0)
GopherItem(type=<ItemType.INFO: 'i'>, display_text='', selector='', host='null.host', port=1)
GopherItem(type=<ItemType.HTML: 'h'>, display_text='Find me all over', selector='URL:https://davep.at/', host='tilde.team', port=70)
GopherItem(type=<ItemType.HTML: 'h'>, display_text='Find me in Geminispace', selector='URL:gemini://tilde.team/~davep/', host='tilde.team', port=70)
GopherItem(type=<ItemType.HTML: 'h'>, display_text='My blog', selector='URL:https://blog.davep.org/', host='tilde.team', port=70)
GopherItem(type=<ItemType.HTML: 'h'>, display_text='finger://plan.cat/davep', selector='URL:finger://plan.cat/davep', host='tilde.team', port=70)
GopherItem(type=<ItemType.HTML: 'h'>, display_text='finger://tilde.team/davep', selector='URL:finger://tilde.team/davep', host='tilde.team', port=70)
GopherItem(type=<ItemType.INFO: 'i'>, display_text='', selector='', host='null.host', port=1)
GopherItem(type=<ItemType.INFO: 'i'>, display_text='My current projects', selector='', host='null.host', port=1)
GopherItem(type=<ItemType.INFO: 'i'>, display_text='~~~~~~~~~~~~~~~~~~~', selector='', host='null.host', port=0)
GopherItem(type=<ItemType.INFO: 'i'>, display_text='', selector='', host='null.host', port=1)
GopherItem(type=<ItemType.HTML: 'h'>, display_text='[Web] Rogallo - A Gemini/Gopher/Finger client for the terminal', selector='URL:https://rogallo.davep.dev/', host='tilde.team', port=70)
GopherItem(type=<ItemType.HTML: 'h'>, display_text='[Gemini] Rogallo - A Gemini/Gopher/Finger client for the terminal', selector='URL:gemini://tilde.team/~davep/rogallo/', host='tilde.team', port=70)
```

See [the main documentation](https://gophermap.davep.dev/) for the full API.

[//]: # (README.md ends here)
