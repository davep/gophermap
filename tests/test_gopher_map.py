"""Tests for the GopherMap class."""

##############################################################################
# Pytest imports.
from pytest import mark, raises

##############################################################################
# Local imports.
from gophermap import GopherMap, GopherMapError
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


##############################################################################
@mark.parametrize(
    "test_map",
    [
        "",
        "Test\r\n.\r\n",
        "!Hello\tworld\tlocalhost\r\n.\r\n",
    ],
)
def test_strict_on_bad_map(test_map: str) -> None:
    """Test that strict mode raises an error on a bad map."""
    with raises(GopherMapError):
        _ = GopherMap(test_map, strict=True).items


##############################################################################
@mark.parametrize(
    "test_map, expected",
    [
        ("iHello\tworld\tlocalhost\t70\r\n3Error\tworld\tlocalhost\t70\r\n.\r\n", True),
        ("iHello\tworld\tlocalhost\t70\r\n.\r\n", False),
        ("3Error\tworld\tlocalhost\t70\r\n.\r\n", True),
        ("This is just some random test", False),
        (".\r\n", False),
        ("", False),
    ],
)
def test_has_error(test_map: str, expected: bool) -> None:
    """Test that has_error returns True if the map contains an error item."""
    assert GopherMap(test_map).has_error is expected


##############################################################################
@mark.parametrize(
    "test_map, expected",
    [
        ("", False),
        ("iHello\tworld\tlocalhost\t70\r\n3Error\tworld\tlocalhost\t70\r\n.\r\n", True),
        ("iHello\tworld\tlocalhost\t70\r\n.\r\n", True),
        ("3Error\tworld\tlocalhost\t70\r\n.\r\n", True),
        ("This is just some random test", False),
        ("Hello\tworld\tlocalhost\t70\r\n.\r\n", False),
        ("hello\tworld\tlocalhost\t70\r\n.\r\n", True),
        (".\r\n", True),
    ],
)
def test_is_likel_a_map(test_map: str, expected: bool) -> None:
    """Test is_likely_a_map returns True if the map is likely a valid Gopher map."""
    assert GopherMap.is_likely_a_map(test_map) is expected


##############################################################################
@mark.parametrize(
    "test_map, expected",
    [
        ("iHello\tworld\tlocalhost\t70\r\n3Error\tworld\tlocalhost\t70\r\n.\r\n", True),
        ("iHello\tworld\tlocalhost\t70\r\n.\r\n", False),
        ("3Error\tworld\tlocalhost\t70\r\n.\r\n", True),
        ("This is just some random test", False),
        ("3. This is just some random test\r\n.\r\n", False),
        (".\r\n", False),
        ("", False),
    ],
)
def test_is_likely_error(test_map: str, expected: bool) -> None:
    """Test that is_likely_error returns True if the map contains an error item."""
    assert GopherMap.is_likely_error(test_map) is expected


### test_gopher_map.py ends here
