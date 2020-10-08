"""
Demonstrate unit testing.
"""


def running_sum(values):
    """Modify values so that it contains the running sums of its original items.

    :param values: a list of integers
    :precondition: values is a list that contains only integers
    :postcondition: the list will be modified to contain a running sum

    >>> some_list = [4, 0, 2, -5, 0]
    >>> running_sum(some_list)
    >>> some_list
    [4, 4, 6, 1, 1]
    """
    for i in range(1, len(values)):
        values[i] = values[i - 1] + values[i]
