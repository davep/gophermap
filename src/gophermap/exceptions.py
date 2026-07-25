"""Exceptions for the library."""


##############################################################################
class GopherMapError(Exception):
    """Base exception for all errors raised by the GopherMap library."""


##############################################################################
class NoFields(GopherMapError):
    """Raised when a Gopher item has no fields."""


### exceptions.py ends here
