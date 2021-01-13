"""
The pprint module lets us "pretty-print" things.

Check out how it prints the dictionary created from this
dictionary comprehension!
"""

import pprint


def make_board(width, height):
    return {(row, column): "This room is empty" for row in range(height) for column in range(width)}


def main():
    board = make_board(5, 5)
    pp = pprint.PrettyPrinter()
    pp.pprint(board)


if __name__ == "__main__":
    main()
