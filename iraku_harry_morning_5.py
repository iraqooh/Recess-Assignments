# Python Inheritance

class Bird:
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        print(f'{self.name} feeds on {food}.')

class Eagle(Bird):
    def move(self):
        print(f'{self.name} moves by walking & flying.')

class Fowl(Bird):
    def move(self):
        print(f'{self.name} moves by walking.')

# Creating objects of the subclass
bird = Bird('A Generic Bird')
baldy = Eagle('Bald Eagle')
rooster = Fowl('Chicken')

# Invoking eat methods
bird.eat('all kinds of food')
baldy.eat('meat')
rooster.eat('seeds & insects')

# Invoking specific move methods
baldy.move()
rooster.move()
print()
#######################################################################

# Example 2
class Vehicle:
    def __init__(self, brand, environment):
        self.brand = brand
        self.environment = environment

    def get_info(self):
        print(f'Brand: {self.brand}\nType: {self.environment}')

    def move(self):
        print(f'{self.brand} is moving.')

class Spacecraft(Vehicle):
    def __init__(self, brand, environment, propulsion):
        super().__init__(brand, environment)
        self.propulsion = propulsion

    # overriding move method
    def move(self, destination):
        print(f'Launching {self.brand} Spacecraft to {destination}.')

vehicle = Vehicle('Generic Vehicle', 'Multi-terrain')
vehicle.get_info()
vehicle.move()

falcon_9 = Spacecraft('Spacex', 'Space', 'Rapter Engines')
falcon_9.get_info()
falcon_9.move('Low Earth Orbit')
print()
########################################################################

# Exercise
from math import pi

print('Exercise')

class Shape:
    def __init__(self, width):
        self.width = width
        print('Shape created')

class Circle(Shape):
    def __init__(self, diameter):
        super().__init__(diameter)
        self.radius = self.width/2

    def get_area(self):
        return pi * self.radius**2
    
    def get_perimeter(self):
        return 2 * pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(width)
        self.length = length
    
    def get_area(self):
        return self.length * self.width
    
    def get_perimeter(self):
        return 2 * (self.length + self.width)
    
circle = Circle(124)
print(f'Area of circle of radius {circle.radius} = {circle.get_area():,.3f} sq. units.')
print(f'Perimeter of circle of radius {circle.radius} = {circle.get_perimeter():,.3f} units.')

plane = Rectangle(97, 54)
print(f'Area of rectangle = {plane.get_area():,.3f} sq. units.')
print(f'Perimeter of rectangle = {plane.get_perimeter():,.3f} units.')
print()
########################################################################

# Multiple inheritance
class Vehicle:
    def __init__(self, brand, environment):
        self.brand = brand
        self.environment = environment

    def get_info(self):
        print(f'Brand: {self.brand}\nType: {self.environment}')

class Propulsion:
    def move(self, method):
        print(f'{self.brand} is propelled by {method}.')

class Car(Vehicle, Propulsion):
    def __init__(self, brand, environment, seats):
        super().__init__(brand, environment)
        self.seats = seats

suv = Car('Cadillac Escalade', 'Terrain', 7)
suv.get_info()
suv.move('Diesel Engine')
print()
#######################################################################

# Method overriding
class Student:
    __tuition = 2500000.0
    def __init__(self, name, id, program):
        self.name = name
        self.id = id
        self.program = program
        self.isEnrolled = False

    def enrol(self, amount):
        if amount > (0.6 * Student.__tuition):
            self.isEnrolled = True
        else: raise ValueError('Tuition amount is insufficient to enrol.')
    
    def register(self, course, time='Day'):
        if self.isEnrolled:
            print(f'{self.name} is now registered for {course}, {time} class.')
        else: print('You are not enrolled.')

class DayStudent(Student):
    def register(self, course):
        return super().register(course)

class EveningStudent(Student):
    def register(self, course, time='Evening'):
        return super().register(course, time)
    
jane = DayStudent('Jane Smith', 3213, 'Computer Science')
try:
    jane.enrol(1500000.0)
except ValueError as e:
    print(e)

try:
    jane.register('Artificial Intelligence')
except ValueError as e:
    print(e)

harry = EveningStudent('Harry Iraku', 7731, 'Software Engineering')
harry.enrol(2000000.0)
harry.register('Software System Design')
print()
#######################################################################

# Polymorphism
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

class Cow(Animal):
    def sound(self):
        print("Moo!")

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()
cow = Cow()

make_sound(dog)
make_sound(cat)
make_sound(cow)

# Abstraction
#prevents instantiation of a class and compels user to override abstract methods in child class
#abstract class has some abstract methods (methods with only declaration but no implementation)

#import abstract base class (abc) package, ABC class and the abstractmethod
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
        
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print('Driving')

    def stop(self):
        print('Stopping')
        
# v = Vehicle(), will not work

c = Car()
c.go()
c.stop()
print()
#######################################################################

# Exercise
print('Exercise')

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(8.28)
rectangle = Rectangle(405.15, 679.16)

print(f'Area of circe of radius {circle.radius} = {circle.area():.3f} sq. units.')
print(f'Area of rectangle = {rectangle.area():,.3f} sq. units.')
print()
########################################################################

# Assignment
# Requirements
# ttk using <pip3 install ttk> or <pip install ttk>
# Supported platforms: Linux, Mac and Windows

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import strftime
from os import path
from subprocess import call
from abc import ABC, abstractmethod

print('Assignment')

class Receiptable(ABC):
    @abstractmethod
    def _open_receipt(self, receipt_name):
        pass
    
class Catalogue:
    def __init__(self):
        self.inventory = {}
        try:
            with open('app_data.txt', 'a+') as file:
                items = ''
                if path.getsize('app_data.txt') == 0:
                    file.writelines(('0\n', 'iPhone 14 Pro:1079.99,USB Cable:2.99,' + 
                        'Flash Disk 16 GB:3.99,Macbook Air M1:1200.00,Beats by Dre:8.79'))
                    file.flush()
                    items = 'iPhone 14 Pro:1079.99,USB Cable:2.99,Flash Disk 16 GB:3.99,Macbook Air M1:1200.00,Beats by Dre:8.79'
                else:
                    file.seek(0, 0)
                    items = file.readlines()[1]
                items = items.split(',')
                for item in items:
                    item = item.split(':')
                    self.inventory.setdefault(item[0], float(item[1]))
        except FileNotFoundError:
            messagebox.showerror('Inventory Error',
                'Inventory file missing!')
            
class Receipt(Receiptable):
    def _open_receipt(receipt_name):
        if path.isfile(receipt_name):
            if Tk().call("tk", "windowingsystem") == "win32":
                # Windows
                call(["notepad.exe", receipt_name])
            elif Tk().call("tk", "windowingsystem") == "x11":
                # Linux (Ubuntu)
                call(["xdg-open", receipt_name])
            elif Tk().call("tk", "windowingsystem") == "aqua":
                # MacOS
                call(["open", receipt_name])

    def __init__(self, customer=None, phone=None, number=None):
        self.__customer = customer
        self.__phone = phone
        self.__number = ''
        if number != None:
            if number < 10:
                self.__number = 'SN00' + str(number)
            elif number < 100:
                self.__number = 'SN0' + str(number)
            else: self.__number = 'SN' + str(number)
        self.__items = []
    
    def get_customer(self):
        return self.__customer
    
    def get_phone(self):
        return self.__phone
    
    def get_items(self):
        return self.__items
    
    def get_number(self):
        return self.__number
    
    def set_name(self, name):
        self.__customer = name

    def set_phone(self, phone):
        self.__phone = phone
            
class ReceiptApplication:
    __inventory = Catalogue()
    __receipts = 0
    __receipt = []
    def __init__(self, title):
        # Getting number of receipts already generated
        try:
            with open('app_data.txt', 'r') as inventory:
                ReceiptApplication.__receipts = int(inventory.readline()[:-1])
        except FileNotFoundError:
            pass
        ReceiptApplication.__receipt = Receipt(number=ReceiptApplication.__receipts + 1)
        # Creating & configuring the window
        self.window = Tk()
        self.window.title(title)
        self.window.geometry('+0+0')
        self.window.config(background='black', padx=16, pady=16, border=8)
        self.window.resizable(0,0)
        # Creating & adding the main frame to the window
        self.main_frame = Frame(self.window)
        self.main_frame.config(background='grey', padx=16, border=4)
        self.main_frame.pack()
        # Creating the labels
        labels = [
            ['Receipt Form', 116, 10, [0, 0, 2, 8]],
            ['Customer Name', 24, 12, [1, 0, 1, 8]],
            ['Phone Number', 24, 12, [2, 0, 1, 1]],
            ['Item', 24, 12, [3, 0, 1, 8]],
            ['Quantity', 24, 12, [4, 0, 1, 8]],
            ['Designed, developed and tested by Iraku Harry\n' + 
                            'Makerere University\n2023', 116, 10, [9, 0, 2, 8]]
        ]

        for config in labels:
            new_label = Label(
                self.main_frame, 
                text=config[0],
                background='#8a8a8a',
                padx=8,
                pady=8,
                width=config[1],
                font=('Tahoma', config[2])
            )
            new_label.grid(
                row=config[3][0],
                column=config[3][1],
                columnspan=config[3][2],
                pady=config[3][3]
            )

        # Creating the entry fields
        input_controls = {
            'name' : [1, 1, 1, 8],
            'phone' : [2, 1, 1, 1],
            'item' : [3, 1, 1, 8],
            'qty' : [4, 1, 1, 8]
        }

        self.input_controls = {}

        for control, config in input_controls.items():
            input_control = None
            if control in ['name', 'phone']:
                input_control = Entry(
                    self.main_frame,
                    width=35,
                    font=('Tahoma', 12)
                )
            elif control == 'item':
                input_control = ttk.Combobox(
                    self.main_frame,
                    values=list(
                        ReceiptApplication.__inventory.inventory.keys()),
                    width=33,
                    font=('Tahoma', 12),
                    state='readonly'
                )
            else:
                input_control = Spinbox(
                    self.main_frame,
                    width=34,
                    from_=1.0,
                    to=100,
                    increment=1.0,
                    font=('Tahoma', 12)
                )
            input_control.grid(
                row=config[0],
                column=config[1],
                columnspan=config[2],
                pady=config[3],
            )
            self.input_controls.setdefault(control, input_control)

        # Creating and adding buttons
        buttons = [
            ['Add Item', 'black', 'silver', 30, 'black', 
                     'silver', self.add_item, [5, 1, 1, 8]],
            ['Generate Receipt', 'black', 'lime', None, 
                    'black', 'lime', self.generete_receipt, [7, 0, 2, 8]],
            ['New Receipt', 'black', 'silver', None, 
                     'black', 'silver', self.new_receipt, [8, 0, 2, 8]],
        ]

        for config in buttons:
            button = Button(
                self.main_frame,
                text=config[0],
                fg=config[1],
                bg=config[2],
                width=config[3],
                command=config[6],
                activebackground=config[4],
                activeforeground=config[5]
            )
            button.grid(
                row=config[7][0], 
                column=config[7][1], 
                columnspan=config[7][2], 
                sticky=NSEW, 
                pady=config[7][3]
            )

        # Creating the item list box
        column_headers = 'item', 'price', 'qty', 'total'
        self.tree = ttk.Treeview(
            self.main_frame,
            columns=column_headers,
            show='headings',
            padding=16
            )
        self.tree.tag_configure(
            'purchases',
            background='silver'
        )

        self.tree.heading('item', text='Item')
        self.tree.heading('qty', text='Qty')
        self.tree.heading('price', text='Price')
        self.tree.heading('total', text='Total')
        self.tree.grid(row=6, column=0, columnspan=2)
        
    
    def launch(self):
        # Launching the program interface
        self.window.mainloop()

    def clear_fields(self):
        self.input_controls.get('qty').delete(0, END)
        self.input_controls.get('qty').insert(0, '1.0')
        self.input_controls.get('item').delete(0, END)
        self.input_controls.get('item').insert(0, '')

    def add_item(self):
        name = self.input_controls.get('name').get()
        phone = self.input_controls.get('phone').get()
        ReceiptApplication.__receipt.set_name(name)
        ReceiptApplication.__receipt.set_phone(phone)
        item = self.input_controls.get('item').get()
        if item not in ReceiptApplication.__inventory.inventory.keys():
            messagebox.showerror('Value Error',
                                  f'{item} is not available!' if item else f'You did not select an item!')
        qty = float(self.input_controls.get('qty').get())
        if qty < 1:
            messagebox.showerror('Quantity Error',
                                  f'Quantity of {item if item else "item"} cannot be zero!')
            self.clear_fields()
        else:
            price = ReceiptApplication.__inventory.inventory.get(item)
            total = price * qty
            price = format(price, '.2f')
            total = format(total, '.2f')
            new_item = [item, price, qty, total]
            ReceiptApplication.__receipt.get_items().append(new_item)
            self.tree.insert('', 0, values=new_item)
            self.clear_fields()

    def new_receipt(self):
        self.input_controls.get('name').delete(0, END)
        self.input_controls.get('phone').delete(0, END)
        self.clear_fields()
        self.tree.delete(*self.tree.get_children())
        ReceiptApplication.__receipt.get_items().clear()

    def generete_receipt(self):
        items = ReceiptApplication.__receipt.get_items()
        if len(items) == 0:
            messagebox.showerror('Empty Receipt Error',
                'No items added to receipt')
        else:
            vat = 0.1
            name = ReceiptApplication.__receipt.get_customer()
            phone = ReceiptApplication.__receipt.get_phone()
            number = ReceiptApplication.__receipt.get_number()
            subtotal = sum(float(item[3]) for item in items)
            total = format(subtotal * 1.1, '.2f')
            subtotal = format(subtotal, '.2f')
            receipt_name = 'receipt' + strftime('%Y-%m-%d-%H%M%S') + '.txt'
            receipt = open(receipt_name, 'w')
            receipt.write(f"\t\t\t\tRECEIPT\n\nSerial Number: {number}\nCustomer: {name}\n" + 
                        f"Phone: {phone}\n\n\nQty\t\t\tItem\t\t\t\t" + 
                        "Unit Price\t\t\t\tLine Total\n")
            for item in items:
                receipt.write(f"{str(item[2]).ljust(22)}{str(item[0]).ljust(30)}{str(item[1]).ljust(32)}" + 
                    f"{item[3]}\n")
            receipt.write(f"\n\t\t\t\t\t\t\t\tSubtotal\t\t\t\t{subtotal}\n\t\t\t\t\t\t\t\t"
                        + f"VAT Tax\t\t\t\t{vat*100}%\n\t\t\t\t\t\t\t\tTotal\t\t\t\t\t" + 
                        f"{total}\n\nDesigned by Iraku Harry\nDepartment of " + 
                        "Networks\nSCIT, COCIS\nMakerere University")
            receipt.flush
            receipt.close()
            self.new_receipt()
            ReceiptApplication.__receipts += 1
            with open('app_data.txt', 'r+') as file:
                file.write(str(ReceiptApplication.__receipts))
            prompt = messagebox.askyesno('Receipt Generated', 
                f'Receipt generated & saved at {path.abspath(receipt_name)}' + 
                '\nDo you want to open the receipt?')
            if prompt: Receipt._open_receipt(receipt_name)

app = ReceiptApplication('Harry\'s Receipt Generator')
app.launch()