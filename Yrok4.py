class Student:
    amount_of_students = 0
    def __init__(self, height=160):
        self.height = height
        Student.amount_of_students += 1
    def grow(self, height=1):
        self.height += height
first_student = Student()
print(first_student.height)
second_student = Student(height=170)
print(second_student.height)
third_student = Student(height=180)
print(third_student.height)
first_student.grow(height=15)
second_student.grow(height=5)
print(first_student.height)
print(second_student.height)
