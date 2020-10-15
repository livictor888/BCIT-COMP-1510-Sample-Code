def find_min_max(values: list):
    """Print the minimum and maximum value from values.

    :param values: a list of things that can be sorted
    :precondition: values is a sortable list of elements
    :postcondition: the min and max values are identified
    """

    min_value = None
    max_value = None
    for value in values:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    print('The minimum value is {0}'.format(min_value))
    print('The maximum value is {0}'.format(max_value))
