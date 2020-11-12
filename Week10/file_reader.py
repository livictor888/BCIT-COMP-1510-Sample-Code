"""
What does this do?
"""


def main():
    filename = 'pi_digits.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())


if __name__ == '__main__':
    main()
