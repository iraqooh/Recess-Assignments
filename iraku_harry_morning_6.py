# Advanced Python Concepts

# Regular Expressions
# Character classes
"""
\d digit 0-9
\w word character
\s whitespace
. any character
* 0 or more occurrences
+ 1 or more occurrences
? 0 or 1 occurrence
[] any character inside bracket
[^ ] any character outside the bracket
\b word boundary
^ match succeeding pattern at the start of the line
$ match preceding pattern at the end of the line
"""
from re import *
# Matching and searching with regex
# Example
x = 'Hello World, Indian Ocean, phone number: +256-773-792-089'
# Matching a word with an 'o' or 'O'
words = findall(r'\w*o+\w*', x, I)
print(words)

# Searching for a phone number
phone = search(r'\+\d{3}(-\d{3})+', x).group()
print(phone)

# Reformatting the phone number
number = sub(r'[+-]', '', phone)
print(number)

# Validating & sanitizing email
def filter_email(email, type=None):
    email = sub(r'^\s+|\s+$', '', email)
    if type == 'Webmail':
        pattern = compile(r'^[a-z]+\.[a-z]+@[a-z]+.mak.ac.ug')
    else: pattern = compile(r'^\w[\w\.-]+@[a-z_]+\.[a-z]{2,6}$')
    matching = match(pattern, email)
    if matching == None: raise ValueError('Invalid email')
    return matching.group()

webmail_1 = '  iraku.harry@students.mak.ac.ug   '
webmail_2 = '  iraku.harry2@mak.ac.ug   '
generic_email_1 = '    iraku123@yahoo.com  '
generic_email_2 = '    iraku123@yahoo.organization  '

try:
    print(filter_email(webmail_1, 'Webmail'))
except ValueError as e:
    print(e)

try:
    print(filter_email(webmail_2, 'Webmail'))
except ValueError as e:
    print(e)

try:
    print(filter_email(generic_email_1))
except ValueError as e:
    print(e)

try:
    print(filter_email(generic_email_2))
except ValueError as e:
    print(e)

# Generators
# Generating multiples of a number
def multiple(number, start=0, stop=10):
    if number > start or number > stop:
        raise ValueError(
            f'Start and stop limits should be larger than {number}')
    for index in range(start, stop):
        if index % number == 0:
            yield index

multiples_of_7 = multiple(7, 7, 100)

from sys import exit

element = ''
while element != 'EOI':
    try:
        print(element, end=' ')
        element = next(multiples_of_7, 'EOI')
    except ValueError as e:
        print(e)
print()

# Iterators
set_of_languages = {'Python', 'C++', 'Java', 'C', 'Kotlin', 'C#'}
iterator = iter(set_of_languages)

lang = ''
while lang != 'EOI':
    print(lang, end=' ')
    lang = next(iterator, 'EOI')
print()

name = 'Iraku Harry'
it = iter(name)
char = ''
while char != 'EOI':
    print(char, end='')
    char = next(it, 'EOI')
print()

def uppercase(func):
    def converter(*args):
        return func(*args).upper()
    return converter

@uppercase
def get_name(name):
    return name.capitalize()

print(get_name('Iraku Harry'))
#######################################################################

# Assignment
def filter_password(password):
    # This function will sanitize and validate a password input
    # By ensuring it has at least 8 and at most 15 alphanumeric characters
    # With at least one symbol
    sanitizing_pattern = compile(r'^\s+|\s+$')
    password = sub(sanitizing_pattern, '', password)
    if len(password) < 8: raise ValueError('Password is too short')
    elif len(password) > 15: raise ValueError('Password is too long')
    validating_pattern = compile(
        r'((?=.*[a-z]+.*)(?=.*[A-Z].*)(?=.*\d+.*)(?=.*[^\d\w\s]+.*))')
    matching = search(validating_pattern, password)
    if matching: return True
    else: raise ValueError('Invalid password')

while True:
    entry = input('Enter password: ')
    try:
        result = filter_password(entry)
        if result: 
            print('Password OK')
            break
    except ValueError as e:
        print(e)

