"""Tests for the item_type module."""

##############################################################################
# Local imports.
from gophermap import ItemType


##############################################################################
def test_unknown_type() -> None:
    """Test that an unknown item type returns ItemType.UNKNOWN."""
    assert ItemType("x") is ItemType.UNKNOWN


### test_item_type.py ends here
