"""Provides tools for working with Gopher maps."""

##############################################################################
# Python imports.
from importlib.metadata import version

######################################################################
# Main library information.
__author__ = "Dave Pearson"
__copyright__ = "Copyright 2026, Dave Pearson"
__credits__ = ["Dave Pearson"]
__maintainer__ = "Dave Pearson"
__email__ = "davep@davep.org"
__version__: str = version("gophermap")
__licence__ = "MIT"

##############################################################################
# Local imports.
from .exceptions import GopherMapError, NoFields
from .gopher_map import GopherMap
from .item import GopherItem
from .item_type import ItemType

##############################################################################
# Exports.
__all__ = [
    "GopherItem",
    "GopherMap",
    "GopherMapError",
    "ItemType",
    "NoFields",
]

### __init__.py ends here
