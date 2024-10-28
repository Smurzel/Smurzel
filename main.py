import random
print("Я весь молодець!")
#1
name = input("Введіть своє ім'я: ")
age = input("Введіть свій вік: ")
print("Привіт", name, ", тобі", age)
#2
age2 = int(input("Введіть свій вік: "))
if age2 < 18:
    print("Вхід заборонено!")
else:
    print("Вхід дозволено!")
#3
d = random.randint(1, 10)
sproba_1 = int(input("Спробуйте вгадати число, що загадав комп'ютер (у вас 3 спроби): "))
if sproba_1 < d:
    print("Більше")
elif sproba_1 > d:
    print("Менше")
elif sproba_1 == d:
    print("Ви вгадали!")
sproba_2 = int(input("Спробуйте ще раз (залишилося 2 спроби): "))
if sproba_2 < d:
    print("Більше")
elif sproba_2 > d:
    print("Менше")
elif sproba_2 == d:
    print("Ви вгадали!")
sproba_3 = int(input("Спробуйте ще раз (залишилася 1 спроба): "))
if sproba_3 < d:
    print("Ви не вгадали!")
elif sproba_3 > d:
    print("Ви не вгадали!")
elif sproba_3 == d:
    print("Ви вгадали!")
#4
for e in range(int(input("Введіть число №1: ")), int(input("Введіть число №1: "))):
    print(e)
#5
def even_numbers_reverse(n):
    even_numbers = [i for i in range(n, 0, -1) if i % 2 == 0]
    print(" ".join(map(str, even_numbers)))
#6
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))
#7
f = int(input("Введіть свою оцінку від 1 до 100: "))
if f == f in range(1,49):
    print("Незадовільно")
elif f == f in range(50,69):
    print("Задовільно")
elif f == f in range(70,89):
    print("Добре")
elif f == f in range(90,100):
    print("Відмінно")
else:
    print("Такого балу не існує")
#8
A = int(input("Введіть число №1: "))
B = int(input("Введіть число №2: "))
C = input("Введіть арефметичну дію (+, -, *, /): ")
if C != "+" or "-" or "*" or "/":
    print("це не арифметична дія!")
if C == "+":
    print(A + B)
elif C == "-":
    print(A - B)
elif C == "*":
    print(A * B)
elif C == "/":
    print(A / B)
elif C == "/" and B == 0:
    print("Ділення на нуль")