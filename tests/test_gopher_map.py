"""Tests for the GopherMap class."""

##############################################################################
# Pytest imports.
from pytest import raises

##############################################################################
# Local imports.
from gophermap import GopherMap, NoFields


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
def test_no_fields() -> None:
    """Test that a Gopher map with no fields raises NoFields."""
    with raises(NoFields):
        _ = GopherMap("x").items


##############################################################################
def test_valid_map() -> None:
    """Test that a valid Gopher map is parsed correctly."""
    gopher_map = GopherMap(raw := "iHello\tworld\tlocalhost\t70\r\n.\r\n")
    assert raw == gopher_map.raw
    assert len(gopher_map.items) == 1
    assert gopher_map.items[0].type.name == "INFO"
    assert gopher_map.items[0].display_text == "Hello"
    assert gopher_map.items[0].selector == "world"
    assert gopher_map.items[0].host == "localhost"
    assert gopher_map.items[0].port == 70


##############################################################################
def test_skip_empty_lines() -> None:
    """Test that empty lines are skipped."""
    gopher_map = GopherMap(raw := "\r\n\r\n.\r\n")
    assert raw == gopher_map.raw
    assert len(gopher_map.items) == 0


### test_gopher_map.py ends here
