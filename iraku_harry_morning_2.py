#decision making
print("Decision Making")
age = int(input('How old are you? '))
if age < 18: print("You are underage")
elif age >= 18 and age <= 65: print("You are an adult")
else: print("You are a mzee!")

#loops
#for loop
print("\nfor Loop")

tup = "Red", "Green", "Yellow", "Blue", "Orange"
for x in tup: print(x)

dict = {"red" : 0xf00, "green" : 0x0f0, "blue" : 0x00f}
for color in dict: print(f"The RGB value for {color} is {dict[color]}")

for i in range(len(tup)): print(tup[i])

for i in range(100, -1, -10): print(i)

#while loop
print("\nwhile Loop")
count = 8
while count >= 0:
    print(count)
    count -= 1

#while True: print('Help! I am stuck in an infinite loop.')

#loop control statements
print("\nLoop Control")
for num in range(0, 20, 2):
    if num == 8 or num == 12: continue
    elif num > 15: break
    print(num)

username = 'harry'
password = '123'
while True:
    name_input = input('Username (harry): ')
    password_input = input('Password (123): ')
    if name_input == username and password_input == password:
        print('Access granted!')
        print(f'Welcome {username}')
        break
    else:
        print('Invalid authentication!')

#Exception handling
print("\nException Handling")
class MyException(Exception):
    def __init__(self, message):
        self. message = message

def login(username, password):
    if username != 'harry' or password != '123': 
        raise MyException('Invalid Authentication Details')
    else: print("Access Granted!")

name = input('Username (harry): ')
password = input('Password (123): ')
try:
    login(name, password)
except MyException as e:
    print(e)
finally:
    print('Exception Handled!')

# Exercise
mental_state = {
    "excited" : "You go man!",
    "anxious" : "Take a deep breath!",
    "blue" : "Don't worry, be happy!",
    "happy" : "I am happy to hear that!",
    "sick" : "Polé"
}

def interpret_emotion(emotion):
    if emotion not in mental_state: raise ValueError('That\'s an abstract feeling!')
    print(mental_state.get(answer))

answer = input('How are you doing today? ')

try:
    interpret_emotion(answer)
except ValueError as e:
    print(e)
finally: print('Have a good day!')

