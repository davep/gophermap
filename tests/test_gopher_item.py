"""Tests for the GopherItem class."""

##############################################################################
# Pytest imports.
from pytest import mark, raises

##############################################################################
# Local imports.
from gophermap import GopherItem, NoFields


##############################################################################
@mark.parametrize(
    "line",
    [
        "",
        "\r\n",
        "\t\r\n",
    ],
)
def test_for_no_fields(line: str) -> None:
    """Test that a GopherItem with no fields raises NoFields."""
    with raises(NoFields):
        _ = GopherItem(line)


##############################################################################
def test_raw() -> None:
    """Test that the raw property returns the original line."""
    item = GopherItem(line := "iHello\tworld\tlocalhost\t70\r\n")
    assert item.raw == line


### test_gopher_item.py ends here
