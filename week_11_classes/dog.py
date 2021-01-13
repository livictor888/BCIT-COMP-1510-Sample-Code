class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.__name = name
        self.__age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.__name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.__namename.title() + " rolled over!")


def main():
    my_dog = Dog('trevor', 6)
    your_dog = Dog('lucy', 3)

    # print("My dog's name is " + my_dog.__name.title() + ".")

    # Report anyone who does this it is a crime against humanity
    print("My dog is " + str(my_dog._Dog__age) + " years old.")
    my_dog.sit()

    print("\nMy dog's name is " + your_dog._Dog__name.title() + ".")
    # Report anyone who does this it is a crime against humanity
    # print("My dog is " + str(your_dog._Dog__age) + " years old.")
    your_dog.sit()


if __name__ == "__main__":
    main()
