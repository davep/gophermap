"""Tests for the item_type module."""

##############################################################################
# Local imports.
from gophermap import ItemType


##############################################################################
def test_unknown_type() -> None:
    """Test that an unknown item type returns ItemType.UNKNOWN."""
    assert ItemType("x") is ItemType.UNKNOWN


##############################################################################
def test_unknown_mime_type() -> None:
    """Test that an unknown item type returns ItemType.UNKNOWN."""
    assert ItemType("x").mime_type == ItemType.UNKNOWN.mime_type


### test_item_type.py ends here
