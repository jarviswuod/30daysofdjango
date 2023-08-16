print('----------------------------')
string1 = 'Django for "Beginners"'
string2 = "Django's for beginners"

paragraph = '''
My name is jarvis
Im a frontend developer
I'm diving into django for the next 30 days
'''

print(f'Introduction part : {paragraph}')

print('----------------------------')
# WORKING WITH STRINGS
course = 'Python for beginners'
print(course[1])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:-2])
print(course[:])  # copying a string

print('----------------------------')
# FORMATTED STRINGS
first_name = 'John'
last_name = 'Smith'
msg = first_name + ' [' + last_name + '] is a coder'
message = f'{first_name} [{last_name}] is a coder'
print(msg)
print(message)

print('----------------------------')
# STRINGS METHODS
course = 'Python for Beginners'
print(len(course))  # Returns the length of the string
print(course.upper())  # converts the string to uppercase # doesn't modify the original string
print(course.lower())  # converts to lowercase  # doesn't modify the original string
print(course.find('o'))  # return the index of the first char or sequence of chars
print(course.find('Beginners'))  # find method is case-sensitive
print(course.find('beginners'))  # returns -1 indicating char not found
print(course.replace('Beginners', 'Absolute Beginners'))  # case-sensitive and replaces the old_char with new_char
print('Python' in course)  # is a boolean expression returning true if 'char' search os present in 'string' else false

print('----------------------------')
# ARITHMETIC OPERATIONS
# # -, +, *, /, %, **
print(10 / 3)  # 3.333333
print(10 % 3)  # 1
print(10 ** 3)  # 1000

x = 10
x = x + 3
x += 3  # does the same job as the top code only in a much shorter way
print(x)  # output 16 coz 10 + 3 + 3

x *= 3
print(x)  # output 48 coz 16 * 3

print('----------------------------')
# OPERATOR PRECEDENCE
# # 1. Parenthesis ()
# # 2. exponential 2 ** 3
# # 3. multiplication & division 2 * 3
# # 4. Addition & subtraction 2 * 3

a = 10 + 3 * 2  # 16
y = 10 ** 4 - 4 / 4  # 9999.0
z = 10 + 3 * 2 ** 2  # 22
w = (10 + 3) * 2 ** 2  # 52

# CHALLENGE 1
b = (2 + 3) * 10 - 3  # 47

print('----------------------------')
# MATH FUNCTIONS
import math

x = 2.9
print(round(x))  # 3 # round to convert to whole numbers
print(abs(x))  # 2.9 # converts any value to a +ve value
print(abs(-2.5))  # 2.5

print(math.floor(2.9))  # 2
print(math.ceil(2.9))  # 3

print('----------------------------')
# IF STATEMENTS
# EXAMPLE 1
is_hot = True
is_cold = False
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print('Have a lovely day')

# EXAMPLE 2
temp = 9
if temp >= 42:
    msg = '''
    It's a hot day
    Drink plenty of water'''
    print(msg)
elif temp <= 10:
    msg = '''
    It's too cold 
    Wear warm clothes'''
    print(msg)
else:
    msg = '''It's a lovely day'''
    print(msg)

# CHALLENGE 2
price = 1000000
has_goodCredit = False
if has_goodCredit:
    down_payment = .1 * price
else:
    down_payment = .2 * price
print(f'Down payment: ${down_payment}')

print('----------------------------')
# LOGICAL OPERATORS
#  # AND: both
#  # NOT
#  # OR: at least one

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_good_credit and has_high_income:
    print('Eligible for loan')

if has_good_credit or has_high_income:
    print('Eligible for loan')

if has_good_credit and not has_high_income:
    print('Eligible for loan')

print('----------------------------')
# COMPARISON OPERATORS
# # >    :less than
# # <    :Greater than
# # >=   :less than or equal to
# # <=   :greater than or equal to
# # ==   :equal to
# # !=   :not equal to

temperature = 30
if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# CHALLENGE 3
# user_name = input("Enter you name: ")
user_name = 'input("Enter you name: ")'
if len(user_name) < 3:
    msg = "Name must be at least 3 characters"
elif len(user_name) > 50:
    msg = 'Name ba a maximum of 50 characters'
else:
    msg = "Name looks good!"
print(msg)

#  # FIRST MINI PROJECT
# PROJECT: Weight Converter

weight = int(input('Weight: '))
weight_unit = input('(L)bs or (K)g: ')
if weight_unit.upper() == 'L':
    weight_Convert = f'{weight * .45} kilos'
elif weight_unit.upper() == 'K':
    weight_Convert = f'{weight / .45} pounds'
print(f'You are {weight_Convert}')
