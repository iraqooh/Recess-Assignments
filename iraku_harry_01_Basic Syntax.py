#Python script

print('Single quoted string')
print("Double quoted string")

#PEP8 guidelines
#snake_case
#camelCase

#this is a single line comment

'''
this is a multi line comment
'''
"""
this is also a multi line comment
"""

#variable declaration & initialization
name = "Iraku Harry"
age = 18
weight = 75.16
isRegistered = True
p = print #assigning an alias to the 'print' function identifier

#basic output
p(f'\n\nName: {name}\nAge: {age}\nWeight: {weight}\nReg. Status: {isRegistered}')
p(age)
p(weight)
p(isRegistered)

#data structures / types

#numbers
#integers with literals 0 to 9, positive or negative
age = 18
p(type(age)) #output <class 'int'>
#floating point literals
pi = 3.14
p(type(pi)) #output <class 'float'>

#strings enclosed between single or double quotes
name = 'Harry'
p(type(name))  #output <class 'str'>

#boolean literals True and False
isOK = False
p(type(isOK))  #output <class 'bool'>

#sequences
#list, enclosed in []
list = [1,2,3]
p(type(list))  #output <class 'list'>

#tuple, enclosed in ()
tup = (1,)
p(type(tup))  #output <class 'tuple'>

#range, for iteration
rng = range(1,6,-2)
p(type(rng))  #output <class 'range'>

#mapping types
#dictionary, pairs of mappings enclosed in {}
dict = {'name':"Harry"}
p(type(dict))  #output <class 'dict'>

#sets, enclosed in {}
set = {True, False}
p(type(set))  #output <class 'set'>

#none type 'None'
object = None
p(type(object))  #output <class 'NoneType'>

p(type(print))  #output <class 'builtin_function_or_method'>

