def operate(operation, first, second):
    return operation(first, second)


def add(first, second):
    """
    Add and return the sum of first and last.

    :param: first
    :param: second
    :return: sum of first and second
    """
    return first + second


def append(first, second):
    return str(first) + str(second)


def prepend(first, second):
    return str(second) + str(first)


def main():
    a = int(input())
    b = int(input())
    c = add
    print(operate(c, a, b))


if __name__ == "__main__":
    main()
