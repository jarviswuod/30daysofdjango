# WHILE LOOPS
i = 1
while i <= 5:
    print(i * '*')
    i = i + 1
print('Done')

print('--------------------------------')
# GUESSING GAME
attempts = 3
correct_num = 9
while attempts > 0:
    # user_input = int(input('Guess: '))
    user_input = 1
    if user_input == correct_num:
        print("You found the gem")
        break
    attempts -= 1
    if attempts == 0:
        print('Sorry you failed')

print('--------------------------------')
# CHALLENGE 1
# CAR GAME
started = False
stopped = True
while True:
    # user_input = input("> ").lower()
    user_input = 'quit'
    if user_input == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif user_input == 'start':
        if started:
            print('Car is already started')
        else:
            print('Car started... Ready to go')
        started = True
        stopped = False
    elif user_input == 'stop':
        if stopped:
            print('Car is already stopped')
        else:
            print('Car stopped.')
        stopped = True
        started = False

    elif user_input == 'quit':
        break
    else:
        print("I don't understand that...")

print('--------------------------------')
# FOR LOOP
for item in 'Python':
    print(item)

print('--------------------------------')
for item in ['mosh', 'john', 'sarah']:
    print(item)

print('--------------------------------')
for item in [1, 2, 3, 4, 5, 6]:
    print(item)

print('--------------------------------')
for item in range(10):
    print(item)

print('--------------------------------')
for item in range(5, 10):
    print(item)

print('--------------------------------')
for item in range(5, 10, 2):
    print(item)

print('--------------------------------')
# CHALLENGE 2
price = [16, 21, 130, 69, 72]
total_price = 0
for item in price:
    total_price += item
print(f'Total: {total_price}')

print('--------------------------------')
# NESTED LOOPS
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

print('--------------------------------')
# CHALLENGE 3
pattern = [5, 2, 5, 2, 2]
for x_count in pattern:
    output = ''
    for number in range(x_count):
        output += '*'
    print(output)

print('--------------------------------')
# LISTS
names = ['john', 'bob', 'Mosh', 'sarah', 'Mary']
names[0] = 'Castro'
print(names[0])
print(names[2])
print(names[-1])
print(names[-2])
print(names[2:4])
print(names[2:])

print('--------------------------------')
# CHALLENGE 4
numbers = [4, 8, 3, 78, 9, 12, 45, 65, 11, 8, 9, 0]
max_value = numbers[0]
min_value = numbers[0]
for value in numbers:
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value
print(max_value)
print(min_value)

print('--------------------------------')
# 2D LISTS
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [4, 5, 6]
]

matrix[0][1] = 20
print(matrix[0][1])

print('--------------------------------')
# LIST METHODS
numbers = [5, 2, 1, 7, 3, 5, 1, 7, 4]
print(numbers)
numbers.append(13)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(5)
print(numbers)
print(numbers.index(1))
print(1 in numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)
print(numbers.count(7))
numbers.clear()
print(numbers)

print('--------------------------------')
# CHALLENGE 5
# REMOVE DUPLICATES IN A LIST
numbers = [10, 10, 10, 10, 5, 2, 1, 7, 7, 2, 3, 13, 3, 5, 1, 7, 4, 13]
no_dup = []
for value in numbers:
    if value not in no_dup:
        no_dup.append(value)
print(no_dup)

print('--------------------------------')
# TUPLES
numbers = (12, 21, 32)
# numbers[0] = 10
print(numbers)
print(numbers[1])

print('--------------------------------')
# UNPACKING
coordinates = (1, 2, 3)

a = coordinates[0]
b = coordinates[1]
c = coordinates[2]
print(a, b, c)

a, b, c = coordinates
print(a, b, c)

print('--------------------------------')
# DICTIONARIES
customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}

print(customer['name'])
# print(customer['birthdate'])  # pops an error coz no key
customer['name'] = "Jarvis"
print(customer.get('birthdate', 'Jan 1 1980'))
print(customer)

print('--------------------------------')
# CHALLENGE 6
# phone_num = (input('Phone: '))
phone_num = '1234jd'
mapping = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero',
}
output = ''
for value in phone_num:
    output += f"{mapping.get(value, '!')} "
print(output)

print('--------------------------------')
# EMOJI CONVERTER
# message = input('>')
message = 'I am sad :( !'
words = message.split(' ')
emojis = {
    ':)': '😊️',
    ':(': '☹️'
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '
print(output)

print('--------------------------------')


# FUNCTIONS


def greet_user():
    print('Hi there')
    print('Welcome aboard')


print("Start")
greet_user()
print("Finish")

print('--------------------------------')


# PARAMETERS
# # 1. POSITIONAL ARGUMENTS


def greet_user(user_name):
    print(f'Hi there {user_name}! Welcome aboard')


greet_user('Jarvis')
greet_user('Mary')
greet_user('Marley')

print('--------------------------------')


# PARAMETERS
# # 2. KEYWORD ARGUMENTS


def greet_user(first_name, last_name):
    print(f'Hi there {first_name} {last_name}! Welcome aboard')


greet_user(last_name='Smith', first_name="John")

print('--------------------------------')


# RETURN STATEMENT
def square(side):
    return side ** 2


print(square(4), square(6))

print('--------------------------------')


# CREATING A REUSABLE CODE
# CHALLENGE 7


def emoji_converter(msg):
    word_split = msg.split(' ')
    emojis_dict = {
        ':)': '😊️',
        ':(': '☹️'
    }
    output_msg = ''
    for word_val in word_split:
        output_msg += emojis_dict.get(word_val, word_val) + ' '
    return output_msg


message = 'I am sad :('
# message = input('>')
print(emoji_converter(message))

print('--------------------------------')
# EXCEPTIONS
try:
    # age = int(input('Age: '))
    age = 0
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be divided by 0')
except ValueError:
    print(f'Invalid value')

print('--------------------------------')


# CLASSES
class Point:
    def move(self):
        print('Move')

    def draw(self):
        print('Draw')


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
point1.move()

point2 = Point()
point1.x = 0
point1.y = 2
print(point1.x)

print('--------------------------------')


# CONSTRUCTORS
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('Move')

    def draw(self):
        print('Draw')


point = Point(10, 20)
print(point.x)
point.x = 11
print(point.x)

print('--------------------------------')


# CHALLENGE 8
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I'm {self.name}")
        print('Talk')


jarvis = Person('Dot Jarvis')
print(jarvis.name)
print(jarvis.talk())

print('--------------------------------')
Dennis = Person('Dennis Shines')
print(Dennis.name)
print(Dennis.talk())

print('--------------------------------')


# INHERITANCE
class Mammal:
    def __init__(self, name, age_):
        self.name = name
        self.age = age_

    def walk(self):
        print('Walk')


class Dog(Mammal):
    def bark(self):
        print('Bark')


class Cat(Mammal):
    def meow(self):
        print('Meow')


dog = Dog('Wendy', 2)
print(dog.name)
print(dog.age)
print(dog.walk())
print(dog.bark())

print('--------------------------------')
cat = Cat('Alfred', 1)
print(cat.name)
print(cat.age)
print(cat.walk())
print(cat.meow())
