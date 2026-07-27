"""Tests for the GopherItem class."""

##############################################################################
# Pytest imports.
from pytest import raises

##############################################################################
# Local imports.
from gophermap import GopherItem, NoFields


##############################################################################
def test_empty_line() -> None:
    """Test that an empty line raises NoFields."""
    with raises(NoFields):
        _ = GopherItem("")


##############################################################################
def test_raw() -> None:
    """Test that the raw property returns the original line."""
    item = GopherItem(line := "iHello\tworld\tlocalhost\t70\r\n")
    assert item.raw == line


### test_gopher_item.py ends here
