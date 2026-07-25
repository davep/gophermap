"""A simple parser to show how the library works."""

##############################################################################
# Python imports.
import fileinput

##############################################################################
# Local imports.
from gophermap import GopherMap


##############################################################################
def parse_input() -> None:
    """Parse the input from stdin or files and print the parsed Gopher map."""
    with fileinput.input() as gopher_map:
        for gopher_item in GopherMap("".join(gopher_map)).items:
            print(f"{gopher_item!r}")


##############################################################################
if __name__ == "__main__":
    parse_input()


### __main__.py ends here
