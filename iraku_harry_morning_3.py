from tkinter import *

p = print

# Python basic operators & expressions

# Arithmetic operators
# addition, +
x = 26.49
y = -17
p(f'x + y = {y + x}')

# subtraction, -
p(f'x - y = {x - y}')

# multiplication, *
p(f'x * y = {x * y}')

# division, /
p(f'x / y = {x / y}')

# floor division, //
p(f'x // y = {x // y}')

# modulus, %
p(f'x % y = {x % y}')

# exponentiation, **
p(f'x ** y = {x ** y}')
p("\n#############################################\n")

# Comparison operators

# equality, ==
p(f'Is x equal to y? {x == y}')

# inequality, !=
p(f'Is x not equal to y? {x != y}')

# less than, <
p(f'Is x less than y? {x < y}')

# less than or equal to, <=
p(f'Is x less than or equal to y? {x <= y}')

# greater than, >
p(f'Is x greater than than y? {x > y}')

# greater than or equal to, >=
p(f'Is x greater than or equal to y? {x >= y}')
p("\n#############################################\n")

# Logical operators
d = True
e = True
f = False

# logical AND, and
p(f'True and False = {d and f}')
p(f'True and true = {d and e}')
p(f'False and false = {f and False}')

# logical OR, or
p(f'True or False = {d or f}')
p(f'True or true = {d or e}')
p(f'False or false = {f or False}')

# logical NOT, not
p(f'Not false = {not f}')
p(f'Not true = {not e}')
p("\n#############################################\n")

# Assignment operators

# assign, =
x = 26.49
p(f'Assign 26.49 to x = = {x}')

# add and assign, +=
x += y
p(f'Add and assign y to x = {x}')

# subtract and assign, -=
x -= y
p(f'Subtract y from x and assign to x = {x}')

# multiply and assign, *=
x *= y
p(f'Multiply x and y and assign to x = {x}')

# divide and assign, /=
x /= y
p(f'Divide x by y and assign to x = {x}')

# floor divide and assign, //=
x //= y
p(f'Floor divide x by y and assign to x = {x}')

# modulus and assign, %=
x %= y
p(f'Divide x by y and assign remainder to x = {x}')

# exponent and assign, **=
x **= y
p(f'Raise x to power of y and assign to x = {x}')
p("\n#############################################\n")

# Membership operator, in
colors = {'red', 'green', 'orange', 'magenta', 'cyan'}
# member of, in
p(f'Yellow is in the Set: {"yellow" in colors}')
p(f'Green is in the Set: {"green" in colors}')
p(f'Blue is not in the Set: {"yellow" not in colors}')
p("\n#############################################\n")

# Identity operator, is

p(f'x is identical to y: {x is y}')
p(f'print is identical to p: {p is print}')
p(f'"28" is identical to 28: {28 is "28"}')
p("\n#############################################\n")

# Bitwise operators
a = 0b1001 #9
b = 0b1110 #14

# bitwise AND, & 
# (sets bit to 1 if both bits are 1)
p(f'Bitwise a and b = {bin(a & b)} = {a & b}')

# bitwise OR, |
# sets bit to 1 if either one of bits is 1
p(f'Bitwise a or b = {bin(a | b)} = {a | b}')

# bitwise XOR, ^
# sets bit to 1 if only one of the bits is 1
p(f'Bitwise a exclusive or b = {bin(a ^ b)} = {a ^ b}')

# bitwise Ones compliment, ~
# reverses bits
p(f'Bitwise ones complement b = {bin(~b)} = {~b}')

# bitwise Left shift, <<
# shifts bits left by specified number
p(f'Bitwise Shift a Left by 2 = {bin(a << 2)} = {a << 2}')

# bitwise Right shift, >>
# shifts bits right by specified number
p(f'Bitwise Shift a Left by 2 = {bin(b >> 2)} = {b >> 2}')

# Assignment (Simple Calculator)

from tkinter import *

window = Tk()
window.geometry("360x640")
window.resizable(0,0)
window.title('Iraku Harry Calculator')
# icon = PhotoImage(file="C:\\Users\\HP\\Documents\\Python with VS Code\\hiraku.png")
# window.iconphoto(True, icon)
result = '0'
expression = '0'
result_frame = Frame(window, height=221)
result_frame.pack(expand=True, fill='both')
result_label = Label(result_frame, 
                    text=result, 
                    anchor=E, 
                    fg='#c1c1c1', 
                    bg='#000000',
                    padx=24,
                    font=('Stencil', 16))
result_label.pack(expand=True, fill='both')
input_label = Label(result_frame, 
                    text=result, 
                    anchor=E, 
                    fg='#c1c1c1', 
                    bg='#202020',
                    padx=24,
                    font=('Stencil', 40, 'bold'))
input_label.pack(expand=True, fill='both')
keypad_frame = Frame(window)
keypad_frame.pack(expand=True, fill='both')
digits = {
    7 : (1,1), 8 : (1, 2), 9 : (1, 3),
    4 : (2,1), 5 : (2, 2), 6 : (2, 3),
    1 : (3,1), 2 : (3, 2), 3 : (3, 3),
    0 : (4,1), '.' : (4, 2)
}
operations = {
    '/' : '\u00f7',
    '*' : '\u00d7',
    '-' : '-',
    '+' : '+'
}

# number, decimal point and equals buttons event handler
def append_expression(value):
    global expression
    if expression == '0': expression = ''
    expression += str(value)
    input_label.config(text=expression[:11])

# defining number buttons, decimal point and equals buttons
for digit, grid_tuple in digits.items():
    button = Button(keypad_frame, text=str(digit), bg='#333333',
                    fg='#ffffff', font=('Stencil', 24, 'bold'),
                    borderwidth=0, command=lambda x=digit: append_expression(x))
    button.grid(row=grid_tuple[0], column=grid_tuple[1], sticky=NSEW)

# arithmetic operator buttons event handler
def append_operator(operator):
    global expression, result
    if result == '0': result = ''
    expression += operator
    result += expression
    expression = ''
    input_label.config(text=expression[:11])
    total = result
    for operator, symbol in operations.items():
        total = total.replace(operator, f' {symbol} ')
    result_label.config(text=total)

# defining arithmetic buttons
i = 0
for operator, symbol in operations.items():
    button = Button(keypad_frame, text=symbol, 
                    font=('Stencil', 20), bg='#ffffff', fg='#000000',
                    borderwidth=0, command=lambda x=operator: append_operator(x))
    button.grid(row=i, column=4, sticky=NSEW)
    i += 1

# clear button event handler
def clear():
    global expression, result
    expression = '0'
    result = '0'
    input_label.config(text=expression[:11])
    total = result
    for operator, symbol in operations.items():
        total = total.replace(operator, f' {symbol} ')
    result_label.config(text=total)

# defining clear button
clear_button = Button(keypad_frame, text='AC', 
                    font=('Stencil', 20), bg='#ff0000', fg='#ffffff',
                    borderwidth=0, command=clear)
clear_button.grid(row=0, column=1, sticky=NSEW)

# backspace event handler
def delete():
    global expression
    expression = expression[:-1]
    input_label.config(text=expression[:11])

# defining backspace button
back_button = Button(keypad_frame, text='C', 
                    font=('Stencil', 20), bg='#333333', fg='#ffffff',
                    borderwidth=0, command=delete)
back_button.grid(row=4, column=3, sticky=NSEW)

# equals button event handler
def evaluate():
    global expression, result
    result += expression
    total = result
    for operator, symbol in operations.items():
        total = total.replace(operator, f' {symbol} ')
    result_label.config(text=total)
    try:
        expression = str(eval(result))
    except Exception as e:
        expression = 'Error'
    finally:
        input_label.config(text=expression[:11])
    result = ''
    input_label.config(text=expression[:11])

# defining equals button
equals_button = Button(keypad_frame, text='=', 
                    font=('Stencil', 20), bg='#00ff00', fg='#202020',
                    borderwidth=0, command=evaluate)
equals_button.grid(row=4, column=4, sticky=NSEW)

# square root button event handler
def sqrt():
    global expression
    expression = str(eval(f'{expression}**0.5'))
    input_label.config(text=expression[:11])

# defining square root button
sqrt_button = Button(keypad_frame, text='\u221ax', 
                        font=('Stencil', 20), bg='#f8faff', fg='#25265e',
                        borderwidth=0, command=sqrt)
sqrt_button.grid(row=0, column=3, sticky=NSEW)

# square button event handler
def square():
    global expression
    expression = str(eval(f'{expression}**2'))
    input_label.config(text=expression[:11])

# defining square button
square_button = Button(keypad_frame, text='x\u00b2', 
                    font=('Stencil', 20), bg='#f8faff', fg='#25265e',
                    borderwidth=0, command=square)
square_button.grid(row=0, column=2, sticky=NSEW)

# stretching buttons to fill up the entire height
# and the entire width of the keypad frame
keypad_frame.rowconfigure(0, weight=1)
for x in range(1, 5):
    keypad_frame.rowconfigure(x, weight=1)
    keypad_frame.columnconfigure(x, weight=1)
window.bind('<Return>', lambda event: evaluate())

# binding buttons to the keyboard keys
for key in digits:
    window.bind(str(key), lambda event, 
                digit=key: append_expression(digit))
for key in operations:
    window.bind(str(key), lambda event, 
                operator=key: append_operator(operator))
    
# launching and displaying app
window.mainloop()