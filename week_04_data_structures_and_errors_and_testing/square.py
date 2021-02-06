"""
A simple doctest example.

Note the location of the import statement.

Note the location of the call to doctest.testmod. We pass verbose=True to it. This is a named
parameter. We will study named parameters later this term. It ensures we see ALL the output.

We WANT to see ALL the output.
"""

import doctest

def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-2)
    4
    >>> square(0)
    0
    >>> square(0.5)
    0.25
    >>> square(-0.5)
    0.25
    """
    return x * x


def main():
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
