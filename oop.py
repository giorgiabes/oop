# Object Orianted Programming in Python


class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + last.lower() + "@ecorp.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def applay_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        ...


emp_1 = Employee("Alice", "Smith", 60000)
print(Employee.num_of_emps)
emp_2 = Employee("Bob", "Green", 50000)
print(Employee.num_of_emps)
