class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    def add_employee(self, *args):
        for employee in args:
            self.employees.append(employee)
    def print_employees_names(self):
        if self.employees != []:
            print(f"Employees of {self.name}.")
            for employee in self.employees:
                print(employee.name, employee.salary, employee.position)
    def delete_employee(self, *args):
        for employee in args:
            self.employees.remove(employee)
    def calculate_total_cost(self, *args):
        print(sum(employee.salary for employee in self.employees))

Max = Employee("Max", 80000, "2D artist")
David = Employee("David", 130000, "Python developer")
Maria = Employee("Maria", 55000, "3D artist")
Mark = Employee("Mark", 90000, "Web developer")
Eva = Employee("Eva", 45000, "C# developer")
IT_Company = Department("IT-Company")
IT_Company.add_employee(Max, David, Maria, Mark, Eva)
IT_Company.delete_employee()
IT_Company.print_employees_names()
IT_Company.calculate_total_cost()