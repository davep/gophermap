"""Provides a class for parsing and holding a Gopher map."""

##############################################################################
# Python imports.
from collections.abc import Iterator
from functools import cached_property
from typing import Final

##############################################################################
# Local imports.
from .exceptions import EmptyMap
from .item import GopherItem

##############################################################################
EOF: Final[str] = "."
"""The EOF marker for a Gopher map."""


##############################################################################
class GopherMap:
    """A class for parsing and holding a Gopher map."""

    def __init__(self, map_text: str, strict: bool = False) -> None:
        """Initialise the Gopher map.

        Args:
            map_text: The text of the Gopher map.
            strict: Whether to be strict about parsing the Gopher map.
        """
        self._raw = map_text
        """The raw text of the Gopher map."""
        self._strict = strict
        """Whether to be strict about parsing the Gopher map."""

    def _parse_map(self, map_text: str) -> Iterator[GopherItem]:
        """Parse the Gopher map text into a list of Gopher items.

        Args:
            map_text: The text of the Gopher map.

        Yields:
            Gopher items.
        """
        if self._strict and not map_text:
            raise EmptyMap("Gopher map is empty")
        for line in map_text.splitlines():
            if line == EOF:
                break
            yield GopherItem(line, self._strict)

    @property
    def raw(self) -> str:
        """The raw text of the Gopher map."""
        return self._raw

    @cached_property
    def items(self) -> tuple[GopherItem, ...]:
        """The list of Gopher items in the map.

        Raises:
            EmptyMap: If the map is empty and strict mode is enabled.
            NoFields: If the line is missing a tab character and strict mode is enabled.
            UnknownItemType: If the item type is unknown and strict mode is enabled.
        """
        return tuple(self._parse_map(self._raw))


### gopher_map.py ends here
