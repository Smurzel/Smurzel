class Human:
    def __init__(self, name = "Human"):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)
    def print_passenger_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passenger.")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}.")
Biba = Human("Biba")
Boba = Human("Boba")
car = Auto("BMW")
car.add_passenger(Biba, Boba)
car.print_passenger_names()
