from car_factory.vehicle import Vehicle


class CarLot:
    def __init__(self):
        self.cars = list()

    def add_new_car(self, vin, name, year, price, odometer):
        temp = Vehicle(vin, name, year, price, odometer)
        self.add_car(temp)

    def add_car(self, car):
        self.cars.append(car)

    def get_cars_list(self):
        return self.cars

    def print_cars(self):
        for car in self.cars:
            print(car)


def main():
    my_lot = CarLot()
    my_lot.add_new_car(123, "Honda", 2020, 20_000, 10_000)
    my_lot.add_new_car("abc", "Toyota", 2018, 15_000, 8_000)

    my_lot.print_cars()
    print("hello")


if __name__ == "__main__":
    main()
