def generate_power(number):
    """
    Examples of use:

    >>> powers_of_two = generate_power(2)
    >>> powers_of_three = generate_power(3)
    >>> print(powers_of_two(7))
    128
    >>> print(powers_of_three(5))
    243
    """

    # Define the inner function ...
    def nth_power(power):
        return number ** power

    # ... that is returned by the factory function.
    return nth_power


def tenth_power(power):
    return 10 ** power


def main():
    tenth_power = generate_power(10)

    print(tenth_power(1))
    print(tenth_power(3))
    print(tenth_power(6))

    powers_of_four = generate_power(4)

    print(powers_of_four(1))
    print(powers_of_four(2))
    print(powers_of_four(3))
    print(powers_of_four(4))
    print(powers_of_four(1/3))


if __name__ == "__main__":
    main()
