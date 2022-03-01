"""
Can you fix this?
"""


def average(values):
    """Return the average of the numbers in values.  Some items in values are
    None, and they are not counted toward the average.

    :param values: a list of numbers that may contain None
    :precondition: values is a list of numbers and/or None
    :return: the average of the non-None numbers in values

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """



if __name__ == '__main__':
    import doctest
    doctest.testmod()
