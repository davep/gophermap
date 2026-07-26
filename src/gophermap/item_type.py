"""Provides an enumeration for the different types of Gopher items."""

##############################################################################
# Future imports.
from __future__ import annotations

##############################################################################
# Python imports.
from enum import StrEnum


##############################################################################
class ItemType(StrEnum):
    """An enumeration for the different types of Gopher items."""

    TEXT = "0"
    """A text file."""
    MENU = "1"
    """A menu."""
    CSO = "2"
    """A CSO phone book."""
    ERROR = "3"
    """An error message."""
    BINHEX = "4"
    """A BinHexed file."""
    DOS_FILE = "5"
    """A DOS file."""
    UUENCODED = "6"
    """A uuencoded file."""
    INDEX_SEARCH = "7"
    """An index search."""
    TELNET = "8"
    """A telnet session."""
    BINARY = "9"
    """A binary file."""
    INFO = "i"
    """An informational message."""
    GIF = "g"
    """A GIF image."""
    IMAGE = "I"
    """An image file."""
    HTML = "h"
    """An HTML file."""
    DOCUMENT = "d"
    """A document file."""
    AUDIO = "s"
    """An audio file."""
    PDF = "P"
    """A PDF file."""
    XML = "X"
    """An XML file."""
    UNKNOWN = "unknown"
    """An unknown type."""

    @classmethod
    def _missing_(cls, value: object) -> ItemType:
        """Handle missing values in the enumeration.

        Args:
            value: The value that is missing.

        Returns:
            The corresponding ItemType for the missing value.
        """
        assert isinstance(value, str)
        return ItemType.UNKNOWN

    @property
    def mime_type(self) -> str:
        """Get the MIME type for the item type.

        Note:
            This is a best-effort mapping and may not be accurate for all
            item types.
        """
        return {
            ItemType.TEXT: "text/plain",
            ItemType.MENU: "text/gopher-menu",
            ItemType.CSO: "text/x-cso",
            ItemType.ERROR: "text/x-error",
            ItemType.BINHEX: "application/mac-binhex40",
            ItemType.DOS_FILE: "application/octet-stream",
            ItemType.UUENCODED: "application/x-uuencode",
            ItemType.INDEX_SEARCH: "text/x-index-search",
            ItemType.TELNET: "application/x-telnet",
            ItemType.BINARY: "application/octet-stream",
            ItemType.INFO: "text/plain",
            ItemType.GIF: "image/gif",
            ItemType.IMAGE: "application/octet-stream",
            ItemType.HTML: "text/html",
            ItemType.DOCUMENT: "application/octet-stream",
            ItemType.AUDIO: "application/octet-stream",
            ItemType.PDF: "application/pdf",
            ItemType.XML: "application/xml",
        }.get(self, "application/octet-stream")


### item_type.py ends here
