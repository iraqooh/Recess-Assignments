# OOP

# Classes
# Creating classes
from math import pi


class Aircraft:
    def __init__(self, type, engines,
                 p_capacity, c_capacity) -> None:
        self.type = type
        self.number_of_engines = engines
        self.passenger_capacity = p_capacity
        self.cargo_capacity = c_capacity

    def taxi(self, direction='in'):
        print(f"Taxi-{direction if direction == 'in' else 'out'}")

    def takeoff(self, passengers=2, weight=0):
        if passengers <= self.passenger_capacity and weight <= self.cargo_capacity:
            print(f'Taking off...ascending')
        else:
            print('Take-off aborted')

    def land(self):
        print('Descending...touchdown...break')


jet = Aircraft('Airplane', 4, 221, 82000)
print(jet.type)
print(jet.number_of_engines)
print(jet.passenger_capacity)
print(jet.cargo_capacity)
jet.taxi()
jet.takeoff(100, 52000)
jet.land()


class Student:
    def __init__(self, name, year, program):
        self.name, self.year, self.program = name, year, program

    def show_details(self):
        print(f'Name:{self.name}\nYear: {self.year}\nProgram: {self.program}')


harry = Student('Iraku Harry', 2, 'BSSE')
harry.show_details()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print('Rectangle created successfully!')

    def get_area(self):
        print(f'Area = {self.width * self.height}')


rectangle = Rectangle(23, 88)
rectangle.get_area()


# Objects

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        print(f'Area = {pi*self.radius**2}')

    def get_circumference(self):
        print(f'Circumference = {pi*self.radius*2}')


circle = Circle(3.46)
circle.get_area()
circle.get_circumference()

# Exercise


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_bonus(self):
        print(f'{self.name}\'s bonus = {self.salary*0.15:,}')


employee1 = Employee('Justine', 150000.0)
employee1.get_bonus()
employee2 = Employee('Mark', 230000.0)
employee2.get_bonus()

# Encapsulation


class User:
    __users = 0

    def __init__(self, username, email, password):
        self.__users += 1
        self.username = username
        self.email = email
        self.password = password

    def get_users(self):
        print(f'Total number of users = {self.__users}')


harry = User('harry', 'harry@abc.com', '1234')
harry.get_users()


class Account:
    __min_withdraw = 5000.0

    def __init__(self, number, balance):
        self._number = number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print('Deposit Success')

    def withdraw(self, amount):
        if self.__min_withdraw <= amount:
            self._balance -= amount
            print('Withdraw Success')
        else:
            print('Insufficient Funds')

    def get_balance(self):
        print(f'Balance = {self._balance}')


harry = Account('4010156489132', 5000.0)
harry.withdraw(2500)
harry.get_balance()
harry.withdraw(45000)
harry.deposit(25000)
print(f'{harry._Account__min_withdraw:,}')

# Exercise


class Temperature:
    def _toFahrenheit(self, temp):
        print(f'{(temp * 9 / 5) + 32} °F')

    def _toCelsius(self, temp):
        print(f'{(temp - 32) * 5 / 9} °C')


reading = Temperature()
reading._toCelsius(212)
reading._toFahrenheit(100)

#######################################################################

# Assignment
print('\n\nAssignment\n')


class Employee:
    __company = 'Makerere University'

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_company(self):
        return Employee.__company

    def give_raise(self, new_salary):
        print(f'{self.__name} has got a raise of {new_salary - self.__salary:,}')
        self.__salary = new_salary


harry = Employee('Harry', 850000)
print(f'{harry.get_name()} works for {harry.get_company()}')
harry.give_raise(1000000)
print(f'{harry.get_name()}\'s new salary is {harry.get_salary():,}.')

try:
    # Trying to access private field __company
    print(Employee.__company)
except AttributeError as e:
    print(f'{e.name} cannot be accessed from outside the Employee class.')

try:
    # Trying to access private field __name
    print(harry.__name)
except AttributeError as e:
    print(f'{e.name} cannot be accessed from outside the Employee class.')
