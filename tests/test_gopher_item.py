"""Tests for the GopherItem class."""

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Local imports.
from gophermap import GopherItem
from gophermap.item_type import ItemType


##############################################################################
@mark.parametrize(
    "line",
    [
        "",
        "\r\n",
        "\t\r\n",
    ],
)
def test_empty_lines_become_info(line: str) -> None:
    """Test that empty lines become INFO items."""
    assert GopherItem(line).type is ItemType.INFO


##############################################################################
def test_raw() -> None:
    """Test that the raw property returns the original line."""
    item = GopherItem(line := "iHello\tworld\tlocalhost\t70\r\n")
    assert item.raw == line


### test_gopher_item.py ends here
