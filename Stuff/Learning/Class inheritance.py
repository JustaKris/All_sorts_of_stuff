class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@ISS.com'

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Kris', 'Bonev', 50000)
emp_2 = Employee('Чочо', 'Попйорданов', 70000)

'''
#Employee.set_raise_amt(1.05)
emp_1.set_raise_amt(1.05) #class methods can also be run from the instance of a class

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
'''

'''
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
'''
#emp_1.raise_amount
#Employee.raise_amount

'''
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

#first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
'''

'''
import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))
'''


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)  #Another option
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Kris', 'Bonev', 50000, 'Python')
dev_2 = Developer('Radostina', 'Elinchova', 650000000, 'JS')

#print(help(Developer))

#print(dev_1.email)
#print(dev_2.email)

'''
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)
'''

mgr_1 = Manager('Venelina', 'Zlateva', 90000, [dev_1])

'''
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()
'''

#print(issubclass(Manager, Employee))

#print(emp_1)

#print(repr(emp_1))
#print(str(emp_1))

#print(emp_1.__repr__())
#print(emp_1.__str__())

'''
print(1+2)

print(int.__add__(1,2))
print(str.__add__('a', 'b'))
'''

print(len('test'))
print('test'.__len__())
print(emp_1 + emp_2)

print(len(emp_1))


