# Exercise 1 (Lists)
# 1
people = ['James', 'Thandi', 'Lucy', 'Chris', 'Bravo']
print(f'Second name in the list is {people[1]}')

# 2
print(f'First name before updating = {people[0]}', end=', ')
people[0] = 'Jane'
print(f'and after updating = {people[0]}')

# 3
people.append('Harry')
print(f'Sixth name is {people[5]}')

# 4
print(f'Third name before adding Bathel is {people[2]}', end=', ')
people.insert(2, 'Bathel')
print(f'and after = {people[2]}')

# 5
print(f'Fourth item before deletion = {people[3]}', end=', ')
del people[3]
print(f'after deletion = {people[3]}')

# 6
print(f'Last item using negative indexing = {people[-1]}')

# 7
numbers = [234,89,74,56,21,65,48]
for index in range(2, 5): 
    print(f'The {index+1}{"rd" if index==2 else "th"} item is {numbers[index]}')

# 8
countries = ['Kenya', 'South Africa', 'Luxembourg']
states = countries.copy()
print(states)

# 9
for country in countries:
    print(country)

# 10
animals = ['Lion', 'Shark', 'Eagle', 'Scorpion']
animals.sort()
print(f'Animals sorted in ascending order: {animals}')
animals.sort(reverse=True)
print(f'Animals sorted in descending order: {animals}')

# 11
for animal in animals:
    if 'a' in animal.lower(): print(f'{animal} has the character "a"')

# 12
firstnames = ['John', 'Harry', 'Jane']
lastnames = ['Smith', 'Iraku', 'Goodwin']
names = firstnames + lastnames
print(names)

# Exercise 2 (Tuples)

# 1
x = ('samsung', 'iphone', 'tecno', 'redmi')
favourite_brand = 'iPhone'

for brand in x:
    if brand == favourite_brand.lower():
        print(f'My favorite phone brand is {brand}.')

# 2
print(f'Penultimate item is {x[-2]}.')

# 3
print(f'Second item before update = {x[1]}', end=', ')
x = list(x)
x[1] = 'itel'
x = tuple(x)
print(f'and after update = {x[1]}.')

# 4
x = list(x)
x.append('Huawei')
x = tuple(x)
print(f'Tuple after adding Huawei = {x}')

# 5
print('Iterating through tuple: ', end=' ')
for brand in x:
    print(brand, end=', ')
print()

# 6
x = list(x)
del x[0]
x = tuple(x)
print(f'Tuple after deleting first item = {x}')

# 7
cities = ['Jinja', 'Arua', 'Entebbe', 'Kampala', 'Mbarara']
cities = tuple(cities)
print(f'Tuple of Ugandan cities: {cities}')

# 8
eastern_city, northern_city, southern_city, capital_city, western_city = cities
print(eastern_city)
print(northern_city)
print(southern_city)
print(capital_city)
print(western_city)

# 9
for index in range(1, 4):
    print(f'The {index+1}{"nd" if index==1 else ("rd" if index==2 else "th")} city is {cities[index]}.')

# 10
firstnames = 'John', 'Harry', 'Jane'
lastnames = 'Smith', 'Iraku', 'Goodwin'
names = firstnames + lastnames
print(names)

# 11
colors = 'blue', 'green'
print(f'Multiplied tuple = {colors*3}')

# 12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(f'Frequency of "8" in {thistuple} = {thistuple.count(8)}.')

# Exercise 3 (Sets)

# 1
beverages = 'Soda', 'Beer', 'Energy Drink', 'Soda', 'Beer'
fav_beverages = set(beverages)
print(f'Set of my favorite beverages = {fav_beverages}.')

# 2
fav_beverages.add('Water')
fav_beverages.add('Milk')
print(f'Set after adding two items = {fav_beverages}.')

# 3
mySet = {'oven', 'kettle', 'microwave', 'refrigerator'}
print(f'Is "microwave" present in the set: {"Yes" if "microwave" in mySet else "No"}.')

# 4
try:
    mySet.remove('kettle')
    print(f'Set after removing \'kettle\' = {mySet}')
except KeyError as e:
    print('Item is not in the set!')

# 5
print(f'Looping through set items: ', end=' ')
for item in mySet:
    print(item, end=', ')

# 6
languages = {'Python', 'C#', 'Assembly', 'BASIC'}
frameworks = ['Laravel', '.NET']
languages.update(frameworks)
print(f'Set after adding List items = {languages}')

# 7
ages = {28, 33, 21, 23}
names = {'Klaus', 'Margo', 'Xavier', 'Jen'}
names_ages = names.union(ages)
print(f'Names after joining with ages = {names_ages}')

# Exercise 4 (Strings)

# 1
name = 'Python v'
version = 3

software = name + str(version)
print(f'Concatenated variables = {software}.')

# 2
txt = " Hello, Uganda! "
stripped_txt = txt.strip().replace(' ', '')
print(f'New text without spaces = {stripped_txt}')

# 3
print(f'Text to uppercase = {txt.upper()}')

# 4
print(f'New text with \'U\' replaced with \'V\' = {txt.replace("U", "V", 1)}')

# 5
y = "I am proudly Ugandan"
print('Characters between 2nd and 4th positions: ', end='')
for index in range(1, 4):
    print(y[index], end=', ')
print()

# 6
x = "All \"Data Scientists\" are cool!"
print(f'String with quotes: {x}')

# Exercise 5 (Dictionaries)

# 1
Shoes = {
    "brand" : "Nick",
    "color" : "black",
    "size" : 40
}

print(f'Shoe size = {Shoes["size"]}')

# 2
Shoes['brand'] = 'Addidas'
print(f'Shoe brand after updating = {Shoes.get("brand")}')

# 3
Shoes.setdefault('type', 'sneakers')
print(f'Dictionary after adding new pair = {list(Shoes.items())}')

# 4
print(f'List of keys = {list(Shoes.keys())}')

# 5
print(f'List of values = {list(Shoes.values())}')

# 6
if Shoes.get('size'): print('Key \'size\' exists in the dictionary!')
else: print('Key \'size\' doesn\'t exist!')

# 7
print('Looping through dictionary: ', end='')
for key, value in Shoes.items():
    print(f'({key} : {value})', end=', ')
print()

# 8
Shoes.pop('color')
print(f'Dictionary after removing \'color\' = {Shoes}')

# 9
Shoes.clear()
print(f'Dictionary after removing all elements = {Shoes}')

# 10
account = {
    'username' : "iraqooh",
    'weight' : 75.48,
    'isRegistered' : False
}

info = account.copy()
print(f'Copied dicitionary = {info}')

# 11
animals = {
    'vertebrates' : {'mammalia', 'pisces'},
    'invertebrates' : {'crustaceans', 'molluscs','insects'}
}

for category in animals:
    print(category, end=': ')
    for group in animals[category]:
        print(group, end=', ')
    print()
