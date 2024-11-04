import random
#1
class Cat:
    def __init__(self, name, age, hunger, energy):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.energy = energy
    def eat(self):
        self.hunger += 20
        self.energy += 10
        if self.hunger > 100:
            self.hunger = 100
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} поїв.")
    def sleep(self):
        self.energy += 50
        self.hunger -= 15
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} поспав.")
    def play(self):
        self.energy -= 25
        self.hunger -= 10
        if self.energy == 0:
            print(f"{self.name} занадто втомлений, щоб гратися.")
        print(f"{self.name} погрався і втомився.")
    def random_event(self):
        events = [
            (self.eat, "попросив у господаря щось смачненьке."),
            (self.sleep, "захотілося подрімати."),
            (self.play, "хоче з вами погратися.")
        ]
        event, description = random.choice(events)
        print(f"{self.name} {description}")
        event()
my_pet = Cat("Кексик", 1, 50, 50)
print({my_pet.hunger}, {my_pet.energy})
my_pet.random_event()
print({my_pet.hunger}, {my_pet.energy})
my_pet.random_event()
print({my_pet.hunger}, {my_pet.energy})
my_pet.random_event()
print({my_pet.hunger}, {my_pet.energy})