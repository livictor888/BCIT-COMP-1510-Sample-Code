"""A module for demonstrating exceptions.

Use common or existing exceptions when possible, i.e.:

IndexError
KeyError
ValueError
TypeError
etc.

Examine the following functions. They all do the same thing, more or less. But as we travel
down the list, the quality of the function increases.

What change(s) do you observe from convert to another_convert to yet_another_convert to
informative_convert?

"""

import sys


def convert(value):
    """Convert to an integer.  Okay. This is fine. Document the behaviour in the docstring."""
    try:
        the_int = int(value)
    except ValueError:
        the_int = -1
    return the_int


def another_convert(value):
    """Convert to an integer.  Better. Safer. Note the use of pass. We want to get rid of this."""
    the_int = -1
    try:
        the_int = int(value)
    except (ValueError, TypeError):
        pass
    return the_int


def yet_another_convert(value):
    """Convert to an integer. Better yet. Clarity and parsimony of code."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return -1


def informative_convert(value):
    """Convert to an integer.  Prints a very helpful error message! Probably best version."""
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        print("Conversion error: {} returning -1".format(str(e)), file=sys.stderr)
        return -1


def our_factorial(positive_integer):
    if positive_integer < 0:
        raise ValueError("No negative numbers!")
    if isinstance(positive_integer, int):
        raise TypeError("That's not an integer")



