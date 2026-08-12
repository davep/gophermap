"""Provides a class for parsing and holding a Gopher map."""

##############################################################################
# Python imports.
from collections.abc import Iterator
from functools import cached_property
from typing import Final

##############################################################################
# Local imports.
from .exceptions import EmptyMap, GopherMapError
from .item import GopherItem
from .item_type import ItemType

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

    @cached_property
    def has_error(self) -> bool:
        """Whether the Gopher map contains an error item.

        Raises:
            EmptyMap: If the map is empty and strict mode is enabled.
            NoFields: If the line is missing a tab character and strict mode is enabled.
            UnknownItemType: If the item type is unknown and strict mode is enabled.

        Note:
            The mentioned exceptions will be raised on accessing this
            property, if in strict mode. If you wish to check for errors
            without raising exceptions, use the [`is_likely_error` class
            method][gophermap.GopherMap.is_likely_error], to test instead.
        """
        return any(item.type is ItemType.ERROR for item in self.items)

    @classmethod
    def is_likely_a_map(cls, text: str) -> bool:
        """Determine if the text is likely a valid Gopher map.

        Args:
            text: The text of the Gopher map.

        Returns:
            True if the text is likely a valid Gopher map, False otherwise.
        """
        try:
            _ = cls(text, strict=True).items
        except GopherMapError:
            return False
        return True

    @classmethod
    def is_likely_error(cls, text: str) -> bool:
        """Determine if the text is likely a Gopher error message.

        Args:
            text: The text to test.

        Returns:
            True if the text is likely a Gopher error message, False otherwise.
        """
        try:
            return cls(text, strict=True).has_error
        except GopherMapError:
            return False


### gopher_map.py ends here
