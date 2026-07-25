"""Provides a class for holding an item in the Gopher map."""

##############################################################################
# Local imports.
from .item_type import ItemType


##############################################################################
class GopherItem:
    """A class for holding an item in the Gopher map."""

    def __init__(self, line: str) -> None:
        """Initialise the Gopher item.

        Args:
            line: The line of text from the Gopher map.
        """
        self._raw = line
        """The raw text of the Gopher item."""
        fields = line.rstrip("\r\n").split("\t")
        self._type = ItemType(fields[0][0] or ItemType.INFO)
        """The type of the Gopher item."""
        self._display_text = fields[0][1:] if len(fields) > 0 else ""
        """The display text of the Gopher item."""
        self._selector = fields[1] if len(fields) > 1 else ""
        """The selector of the Gopher item."""
        self._host = fields[2] if len(fields) > 2 else ""
        """The host of the Gopher item."""
        self._port = int(fields[3]) if len(fields) > 3 and fields[3].isdigit() else 70
        """The port of the Gopher item."""

    @property
    def type(self) -> ItemType:
        """The type of the Gopher item."""
        return self._type

    @property
    def display_text(self) -> str:
        """The display text of the Gopher item."""
        return self._display_text

    @property
    def selector(self) -> str:
        """The selector of the Gopher item."""
        return self._selector

    @property
    def host(self) -> str:
        """The host of the Gopher item."""
        return self._host

    @property
    def port(self) -> int:
        """The port of the Gopher item."""
        return self._port

    def __repr__(self) -> str:
        """Return a string representation of the Gopher item."""
        return (
            f"GopherItem(type={self.type!r}, display_text={self.display_text!r}, "
            f"selector={self.selector!r}, host={self.host!r}, port={self.port!r})"
        )


### item.py ends here
