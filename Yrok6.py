number_1 = float(input("Введіть 1 число:"))
number_2 = float(input("Введіть 2 число:"))
arithmetic_operation = input("Введіть арифметичну дію (+, -, *, /, ^:")
if arithmetic_operation == "+":
    print(number_1 + number_2)
elif arithmetic_operation == "-":
    print(number_1 - number_2)
if arithmetic_operation == "*":
    print(number_1 * number_2)
elif arithmetic_operation == "/":
    print(number_1 - number_2)
elif arithmetic_operation == "^":
    print(number_1 ** number_2)
else:
    print("Це не арифметична дія!")
