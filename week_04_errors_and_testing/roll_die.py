"""
Demonstrate how to mock an object.
"""

import random


def roll_die(rolls, sides):
    """
    Roll a die with the specified number of sides the specified number of times.

    :param rolls: an int
    :param sides: an int
    :precondition: a must be an int
    :precondition: b must be an int
    :postcondition: calculate the sum of a and b
    :return: the sum of the arguments
    """
    return random.randint(rolls, sides * rolls)
