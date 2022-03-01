"""
Cool things we can do with list and range functions.
"""


def print_table(size):
    """Print the multiplication table for numbers 1 through n inclusive.

    >>> print_table(5)
        1   2   3   4   5
    1   1   2   3   4   5
    2   2   4   6   8   10
    3   3   6   9   12  15
    4   4   8   12  16  20
    5   5   10  15  20  25
    """
    numbers = list(range(1, size + 1))

    for number in numbers:
        print('\t' + str(number), end='')
    print()

    for number in numbers:
        print(number, end='')
        for other_number in numbers:
            print('\t' + str(number * other_number), end='')
        print()

# Can you explain to me how this works?
