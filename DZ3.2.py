from itertools import product


class Product:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability
class Cart:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, *args):
        for product in args:
            self.products.append(product)
    def print_product_names(self):
        if self.products != []:
            print(f"Products of {self.name}.")
            for product in self.products:
                print(product.name, product.price, product.availability)
        else:
            print(f"There are no passengers in {self.name}.")
    def delete_product(self, *args):
        for product in args:
            self.products.remove(product)
    def calculate_total_cost(self, *args):
        print(sum(product.price for product in self.products))

milk = Product("milk", 45, "available")
cheese = Product("cheese", 80, "available")
sausage = Product("sausage", 80, "available")
bottle_of_water = Product("bottle_of_water", 20, "available")
tea = Product("tea", 50, "available")
coffee = Product("coffee", 60, "available")
bread = Product("bread", 25, "available")
eggs = Product("eggs", 30, "available")
butter = Product("butter", 70, "available")
mayonnaise = Product("mayonnaise", 35, "available")
ketchup = Product("ketchup", 35, "available")
pasta = Product("pasta", 40, "available")
cart = Cart("Кошик №1")
cart.add_product(milk, cheese, sausage, bottle_of_water,
                 tea, coffee, bread, eggs, butter, mayonnaise, ketchup)
cart.delete_product()
cart.print_product_names()
cart.calculate_total_cost()