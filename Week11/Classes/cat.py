class Cat:
    """
    Meow. This class represents a Cat.
    """

    counter = 0

    def __init__(self, name: str, age: int):
        self.name = name

        if age < 0:
            raise ValueError("Cats cannot have a negative age, try again!")
        else:
            self.age_in_years = age

        self.id = Cat.counter
        Cat.counter += 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age_in_years

    def print_info(self):
        print("I am a cat.  My ID is " + str(self.id) +
              " and there are this many cats in the universe: " + str(Cat.counter))


def main():
    print(Cat.counter)

    try:
        one = Cat("Mr. Snuggle-bunny", -1)
    except ValueError:
        print("NO! Bad kitty!")
    two = Cat("Duchess", 8)
    three = Cat("Cleo", 8)

    # one.print_info()
    two.print_info()
    three.print_info()

    print(three.counter)
    # print(one.counter)


if __name__ == "__main__":
    main()
