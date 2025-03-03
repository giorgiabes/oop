# Object Orianted Programming in Python


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + last.lower() + "@ecorp.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("Alice", "Smith", 60000)
emp_2 = Employee("Bob", "Green", 50000)

print(Employee.fullname(emp_1))
print(emp_1.fullname())