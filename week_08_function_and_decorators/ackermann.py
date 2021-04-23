"""
The Ackermann function is a famous recursive mathematical algorithm.

It does nothing.

It just creates a recursive call stack that grows and shrinks, sometimes for a very long time.
"""


def ackermann(first, second):
    if first == 0:
        return second + 1
    elif second == 0:
        return ackermann(first - 1, 1)
    else:
        return ackermann(first - 1, ackermann(first, second - 1))


def main():
    ackermann(3, 3)


if __name__ == "__main__":
    main()
