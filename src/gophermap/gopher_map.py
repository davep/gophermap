"""Provides a class for parsing and holding a Gopher map."""

##############################################################################
# Python imports.
from collections.abc import Iterator
from functools import cached_property
from typing import Final

##############################################################################
# Local imports.
from .item import GopherItem

##############################################################################
EOF: Final[str] = "."
"""The EOF marker for a Gopher map."""


##############################################################################
class GopherMap:
    """A class for parsing and holding a Gopher map."""

    def __init__(self, map_text: str) -> None:
        """Initialise the Gopher map.

        Args:
            map_text: The text of the Gopher map.
        """
        self._raw = map_text
        """The raw text of the Gopher map."""

    @staticmethod
    def _parse_map(map_text: str) -> Iterator[GopherItem]:
        """Parse the Gopher map text into a list of Gopher items.

        Args:
            map_text: The text of the Gopher map.

        Yields:
            Gopher items.
        """
        for line in map_text.splitlines(keepends=True):
            if line.strip() == EOF:
                break
            if line.strip():
                yield GopherItem(line)

    @property
    def raw(self) -> str:
        """The raw text of the Gopher map."""
        return self._raw

    @cached_property
    def items(self) -> tuple[GopherItem, ...]:
        """The list of Gopher items in the map."""
        return tuple(self._parse_map(self._raw))


### gopher_map.py ends here
