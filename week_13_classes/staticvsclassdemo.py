class ShippingContainer:
    next_serial = 0

    @staticmethod
    def _get_next_serial():
        """
        A static method does not accept the cls parameter.
        A static method cannot access or modify a class state.
        It behaves like a plain old function.
        It's only here because it makes sense to be inside the class.
        Basically useless.
        """
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @classmethod
    def _get_next_serial(cls):
        """
        A class method takes cls as its first parameter.
        It is bound to the class, not an instance of the class.
        Can modify state of class level variables.

        We use class methods for factory methods (COMP 2522).
        """
        result = cls.next_serial
        cls.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()


def main():
    a_container = ShippingContainer("YML", "coffee")
    print(a_container.serial)
    print(ShippingContainer.next_serial)
    print(ShippingContainer._get_next_serial())
    print(ShippingContainer.next_serial)


if __name__ == "__main__":
    main()
