import random


class Die:
    """A simple attempt to model a die."""

    def __init__(self, face_value, number_of_sides):
        self.face_value = face_value
        self.number_of_sides = number_of_sides

    def get_face_value(self):
        return self.face_value

    def set_face_value(self, new_value):
        if 0 < new_value <= self.number_of_sides:
            self.face_value = new_value

    def get_number_of_sides(self):
        return self.number_of_sides

    def set_number_of_sides(self, new_size):
        if new_size > 0:
            self.number_of_sides = new_size

    def roll_die(self):
        self.face_value = random.randint(1, self.number_of_sides)
        return self.get_face_value()


def main():
    my_die = Die(6, 6)
    print(my_die.roll_die())
    my_die.set_number_of_sides(-1)
    print(my_die.get_number_of_sides())


if __name__ == "__main__":
    main()

# Here's the same thing in module and function form

# import random
#
# face_value = 1
# number_of_sides = 1
#
# """A module.  This module represents a die."""
# def get_face_value():
#     return face_value
#
#
# def set_face_value(new_value):
#     global face_value
#     if 0 < new_value <= number_of_sides:
#         face_value = new_value
#
#
# def get_number_of_sides():
#     return number_of_sides
#
#
# def set_number_of_sides(new_size):
#     global number_of_sides
#     if new_size > 0:
#         number_of_sides = new_size
#
#
# def roll_die():
#     global face_value
#     face_value = random.randint(1, number_of_sides)
#     return get_face_value()
