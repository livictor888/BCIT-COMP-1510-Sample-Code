"""
We raise errors in functions when we want the caller to deal with the problem.

The caller of the function must use try-except to deal with it and prevent
the program from crashing.
"""


def capitalize_name(name):
    if len(name) == 0:
        raise ValueError('No empty names allowed!')
    else:
        return name.title()


def main():

    capitalized_name = capitalize_name("nicole paige brookes")
    print(capitalized_name)

    try:
        another_capitalized_name = capitalize_name("")
    except ValueError as e:
        print(e)
    else:
        print(another_capitalized_name)


if __name__ == "__main__":
    main()
