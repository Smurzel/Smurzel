import random
class Human:
    def __init__(self, name="None", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brand_list)

class Pet:
    def __init__(self, name="None"):
        self.name = name
        self.energy = 100
        self.gladness = 50
        self.satiety = 50
    def eat(self):
        self.satiety += 20
        self.energy += 10
        if self.satiety > 100:
            self.satiety = 100
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} поїв.")
    def sleep(self):
        self.energy += 50
        self.satiety -= 15
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} поспав.")
    def play(self):
        self.energy -= 25
        self.satiety -= 10
        if self.energy == 0:
            print(f"{self.name} занадто втомлений, щоб гратися.")
        print(f"{self.name} погрався і втомився.")

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False
class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

brand_list = {"BMW":{"fuel":100, "strength":100,"consumption": 6},
"Lada":{"fuel":50, "strength":40,"consumption": 10},
"Volvo":{"fuel":70, "strength":150,"consumption": 8},
"Ferrari":{"fuel":80, "strength":120,"consumption": 14},
"Mercedes":{"fuel":90, "strength":100,"consumption": 8}}

job_list = {"Java developer":{"salary":50, "gladness_less": 10 },
"Python developer":{"salary":40, "gladness_less": 3 },
"C++ developer":{"salary":45, "gladness_less": 25 },
"C# developer":{"salary":40, "gladness_less": 25 },
"Rust developer":{"salary":70, "gladness_less": 1 },}