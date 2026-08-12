"""Provides exceptions for the Gopher map."""


##############################################################################
class GopherMapError(Exception):
    """Base class for Gopher map errors."""


##############################################################################
class EmptyMap(GopherMapError):
    """Raised when a Gopher map is empty."""


##############################################################################
class NoFields(GopherMapError):
    """Raised when a Gopher item has no fields."""


##############################################################################
class UnknownItemType(GopherMapError):
    """Raised when a Gopher item has an unknown type."""


### exceptions.py ends here
