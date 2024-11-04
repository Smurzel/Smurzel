#1
a = int(input("Введіть суму поповнення: "))
b = int(input("Введіть суму зняття: "))
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self):
        self.balance += a
    def withdraw(self):
        if self.balance < b:
            print("Ваш баланс менше, ніж сума зняття!")
        else:
            self.balance -= b
my_bank_account = BankAccount("1234 5678 9012 3456", 500)
print({my_bank_account.account_number}, {my_bank_account.balance})
my_bank_account.deposit()
print({my_bank_account.account_number}, {my_bank_account.balance})
my_bank_account.withdraw()
print({my_bank_account.account_number}, {my_bank_account.balance})
#2
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        print({self.make}, {self.model}, {self.year})
bmw = Car("bmw", "x5", "1999 рік")
mercedes_benz = Car("mercedes-benz", "w213", "2016 рік")
bmw.get_info()
mercedes_benz.get_info()
#3
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def get_salary_info(self):
        print("Заробітна плата", {self.name},"а:", {self.salary})
Oleksandr = Employee("Олександр", "Стоматолог", "35000 грн")
Maxim = Employee("Максим", "Лікар", "25000 грн")
Oleksandr.get_salary_info()
Maxim.get_salary_info()
#4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
rectangle = Rectangle(5, 10)
print("Площа прямокутника =", rectangle.calculate_area())
print("Периметр прямокутника =", rectangle.calculate_perimeter())
#5
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
    def display_info(self):
        print({self.name}, {self.price}, {self.quantity})
product1 = Product("Молоко", 45, 2)
print("Загальна вартість товарів =", product1.calculate_total_price())
product1.display_info()
