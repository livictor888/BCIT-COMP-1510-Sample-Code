class Vehicle:
    def __init__(self, vin, name, year, price, odometer):
        self.vin = vin
        self.name = name
        self.year = year
        self.price = price
        self.odometer = odometer

    def get_vin(self):
        return self.vin

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    def get_odometer(self):
        return self.odometer

    def __str__(self):
        string = f"Vin: {self.vin}, Name: {self.name}, " \
                 f"Year: {self.year}, Price: {self.price}, Odometer: {self.odometer}"
        return string
