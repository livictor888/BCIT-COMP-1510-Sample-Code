import math


class Circle:

    """
    Create a Circle object.
    """
    def __init__(self, x: int, y: int, radius: int):
        self.__x = x
        self.__y = y
        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError("You cannot give a radius below zero")

    """
    Get X Value.
    """
    def get_x(self):
        return self.__x

    """
    Get Y Value.
    """
    def get_y(self):
        return self.__y

    """
    Get Radius.
    """
    def get_radius(self):
        return self.__radius

    """
    Set X Coordinate.
    """
    def set_x(self, x_input: int):
        self.__x = x_input

    """
    Set Y Coordinate.
    """
    def set_y(self, y_input: int):
        self.__y = y_input

    """
    Set Radius.
    """
    def set_radius(self, radius_input: int):
        if radius_input > 0:
            self.__radius = radius_input
        else:
            raise ValueError("You can't give a input of below zero")

    """
    Get Circumference
    """
    def get_circumference(self):
        return 2 * math.pi * self.__radius

    """
    Get Area
    """
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    """
    Print out Info
    """
    def __str__(self):
        return 'X: ' + str(self.__x) + " Y: " + str(self.__y) + " Radius: " + str(self.__radius)


def main():
    try:
        Circle(0, 0, 0)
    except ValueError:
        print('You cannot give a radius below zero')

    try:
        Circle(0, 0, 1)
        print('It worked')
    except ValueError:
        print('You cannot give a radius below zero')

    yeet = Circle(1, 1, 2)
    print(yeet.get_x())
    print(yeet.get_y())
    print(yeet.get_radius())

    yeet.set_x(1)
    yeet.set_y(1)
    yeet.set_radius(1)

    print(yeet.get_x())
    print(yeet.get_y())
    print(yeet.get_radius())

    print(yeet.get_circumference())
    print(yeet.get_area())

    print(yeet)


if __name__ == "__main__":
    main()

