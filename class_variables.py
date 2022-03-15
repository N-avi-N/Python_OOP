class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee('John', 'Doe', 50000)
emp_2 = Employee('Jenny', 'Doe', 60000)

print(Employee.num_of_emps)


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

