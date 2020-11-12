class ShippingContainer:
    next_serial = 1337

    # @staticmethod
    # def _get_next_serial():
    #     result = ShippingContainer.next_serial
    #     ShippingContainer.next_serial += 1
    #     return result

    @classmethod
    def _get_next_serial(cls):
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


if __name__ == "__main__":
    main()
