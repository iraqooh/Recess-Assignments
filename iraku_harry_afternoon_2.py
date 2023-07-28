import re

p = print

#Python dictionaries, for storage multiple key-value pairs

prices = {
    'Tesla' : 94.64,
    'Bitcoin' : 23564.45,
    'Amazon' : 123.79,
    'Microsoft' : 312.54,
    'Alpahbet' : 1034.94,
    'Apple' : 215.46
}

tickers = {
    'Tesla' : 'TSLA',
    'Bitcoin' : 'BTC',
    'Amazon' : 'AMZN',
    'Microsoft' : 'MSFT',
    'Alpahbet' : 'GOOGL',
    'Apple' : 'AAPL'
}

p(tickers)

#dictionary creation using explicit dictionary comprehension
faang = {
    key : "FAANG" for (key, value) in prices.items()
}
p(faang)

#dictionary creation using dictionary comprehension and conditional statement
faang = {
    key : 'Billion Dollar' if value < 500 
    else 'Trillion Dollar' for (key, value) in prices.items()
}
p(faang)

#dictionary creation using dictionary comprehension 

#number of items
p(len(tickers))

#data type
p(type(prices))
p(type(tickers) == dict)

#accessing elements
#using slice operator
p(prices['Apple'])

#using setdefault
p(prices.setdefault('Bitcoin'))

#using get method
p(prices.get('Apple'))

#getting list of keys and values
p(tickers.keys())
p(tickers.values())


#getting list of all items
p(tickers.items())

#copying
new_dict = tickers.copy()
p(new_dict)

#removing items using del
# del new_dict['Alphabet']

#removing items using clear
new_dict.clear()
p(new_dict)

########################################################################

# Exercise 1
p(list(prices.values()))

# Exercise 2
p('Available' if 'Bitcoin' in tickers else 'Unavailable')

# Exercise 3
#updating using slice operator
tickers['Apple'] = 'APLE'
p(tickers.get('Apple'))

#updating using setdefault
prices.setdefault('Visa', 12.45)
p(prices.get('Visa'))
p(prices.get('AT&T'))

#updating by adding another dictionary
new_items = {'SnapChat' : 'SNAP', 'Twitter' : 'TWT'}
tickers.update(new_items)
p(tickers)

# Exercise 4
# adding key-pairs
prices.setdefault('Facebook', 25.88)
p(prices.get('Facebook'))

# Exercise 5
# looping 1/2
for key, value in prices.items(): 
    p(f'The stock price of {key} is ${value}')

# looping 2/2
for key in tickers: 
    p(f'The ticker symbol for {key} is {tickers[key]}')

# Nesting
inner_prices = {
    'Tesla' : 94.64,
    'Bitcoin' : 23564.45,
    'Amazon' : 123.79
}

inner_symbols = {
    'Tesla' : 'TSLA',
    'Bitcoin' : 'BTC',
    'Amazon' : 'AMZN'
}
nested_dict = {
    'prices' : inner_prices,
    'symbols' : inner_symbols
}

p(nested_dict.get('prices').get('Tesla'))
p(nested_dict.get('symbols'))

for property in nested_dict:
    for key, value in nested_dict.get(property).items():
        p(f'{key} : {value}')

########################################################################

def get_type(*values):
    for value in values:
        p(f'The type of {value} is {type(value)}')

# Python Numbers
a = 28
b = -66
get_type(a, b)

# floats
c = 3.14
d = -0.975
e = 6.02E23
get_type(c, d, e)

# complex
e = 1-5j
f = 1j
get_type(e, f)

# type conversion
# int to complex
g = complex(a)
p(type(g))
g = complex(b, -2)
p(type(g))

# int to float
g = float(a)
p(type(g))

# float to complex
g = complex(d, 3)
p(type(g))

# complex to int
g = int(e.real)
p(g)

# type casting
n = int(22)
n = int('28')
p(type(n))

# Python strings
name = 'Harry'
language = "Python"

# dir = """C:\Users\HP\Documents\Python with VS Code> c:; 
#     cd 'c:\Users\HP\Documents\Python with VS Code';noon_2.py'"""
# p(dir)

name = 'O\'Shea'
print(name) # output: O'Shea

name = r'O\'Shea'
print(name) # output: O\'Shea

#####################################################################

# Exercise 1
word = 'antidisestablishmentarianism'
p(len(word))

# Exercise 2
for character in word:
    print(character, end=' ')
p()
for index in range(len(word)-1, -1, -1):
    p(word[index], end='')
p()
# Exercise 3
p(f'Character at index 8 is {word[8]}')
p(f'Charactes from index 8 are {word[8:]}')
p(f'Charactes up to index 8 are {word[:8]}')
p(f'Charactes between indices 2 and 8 are {word[2:8]}')
p(f'Charactes up to third last index are {word[:-2]}')

######################################################################

# modifying strings
name = ' iraku harry,  '
formal = name.capitalize()
p(formal)
uppercase = name.upper()
p(uppercase)
lowercase = uppercase.lower()
p(lowercase)
username = name.strip()
p(username)
username = username.strip(',')
p(username)
username = re.sub('\s*', '', username)
p(username)

# concatenation
firstname = 'Jane'
lastname = 'Smith'
name = firstname + ' ' + lastname
p(name)

# formatted strings and interpolation
greeting = f'Hello {firstname}, welcome to Python Programming.'
p(greeting)
greeting = 'Hello ' + firstname + ', welcome to Python Programming.'
p(greeting)
greeting = 'Hello {}, welcome to Python Programming.'
p(greeting.format(firstname))

#boolean type
isOk = False
p(not isOk)
p(23.11 >= 23)
p('25' == 25)
p(bool(0))
p(bool(''))
p(bool(-4))
p(bool(print))

######################################################################

# Exercise 
age = 17.5

if age < 18: print('Child')
elif age >= 18 and age <= 65: print('Adult')
else: print('Mzeé')

#####################################################################


