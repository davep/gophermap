"""Tests for the GopherMap class."""

##############################################################################
# Local imports.
from gophermap import GopherMap
from gophermap.item_type import ItemType


##############################################################################
def test_empty_map() -> None:
    """Test that an empty Gopher map has no items."""
    gopher_map = GopherMap("")
    assert gopher_map.items == ()


##############################################################################
def test_eof_only_map() -> None:
    """Test that a Gopher map with only the EOF marker has no items."""
    gopher_map = GopherMap(".\r\n")
    assert gopher_map.items == ()


##############################################################################
def test_valid_map() -> None:
    """Test that a valid Gopher map is parsed correctly."""
    gopher_map = GopherMap(raw := "iHello\tworld\tlocalhost\t70\r\n.\r\n")
    assert raw == gopher_map.raw
    assert len(gopher_map.items) == 1
    assert gopher_map.items[0].type is ItemType.INFO
    assert gopher_map.items[0].display_text == "Hello"
    assert gopher_map.items[0].selector == "world"
    assert gopher_map.items[0].host == "localhost"
    assert gopher_map.items[0].port == 70


##############################################################################
def test_empty_lines_become_info() -> None:
    """Test that empty lines become INFO items."""
    gopher_map = GopherMap(raw := "\r\n\r\n.\r\n")
    assert raw == gopher_map.raw
    assert len(gopher_map.items) == 2
    assert gopher_map.items[0].type is ItemType.INFO
    assert gopher_map.items[0].display_text == ""
    assert gopher_map.items[0].selector == ""
    assert gopher_map.items[0].host == ""
    assert gopher_map.items[0].port == 70
    assert gopher_map.items[1].type is ItemType.INFO
    assert gopher_map.items[1].display_text == ""
    assert gopher_map.items[1].selector == ""
    assert gopher_map.items[1].host == ""
    assert gopher_map.items[1].port == 70


##############################################################################
def test_allow_lines_without_tabs() -> None:
    """Test that lines without tabs are allowed.

    https://github.com/davep/rogallo/discussions/241
    """
    gopher_map = GopherMap(raw := "iHello\r\n.\r\n")
    assert raw == gopher_map.raw
    assert len(gopher_map.items) == 1
    assert gopher_map.items[0].type is ItemType.INFO
    assert gopher_map.items[0].display_text == "Hello"
    assert gopher_map.items[0].selector == ""
    assert gopher_map.items[0].host == ""
    assert gopher_map.items[0].port == 70


### test_gopher_map.py ends here
