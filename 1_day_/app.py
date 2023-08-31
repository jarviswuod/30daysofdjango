# INTRODUCTION
print('Dot Jarvis')
print('*' * 10)

# VARIABLES
# # boolean
# # integer
# # string
is_raining = True
is_shinning = False
likes = 10
likes = 20
names = 'Jarvis'
print(is_raining)
print(names)
print(likes)

# CHALLENGE 1
full_name = 'John Smith'
age = 20
is_newPatient = True

# GETTING INPUT FROM USER
name = input("What's you name ? ")
print('Hi ' + name)

# CHALLENGE 2
name = input('Whats your name again? ')
user_color = input('Whats your favourite color? ')
print(name + ' favourite color is ' + user_color)

# TYPE CONVERSION
birth_date = int(input("Enter your Birth date "))
age = 2023 - birth_date
print('age: ' + age)

# CHALLENGE 3
length = int(input('Enter length in meters: '))
len_cm = length * 100
print(f"{length}meters is {len_cm}cm")

# STRINGS
statement = 'Python course for "beginners"'
statement = "Python's course for beginners"
multiline = '''
FirstLine
SecondLine
...

Last line
'''

course = 'Python course'
print(course[0])
print(course[-1])
print(course[-2])

print(course[0:3])
print(course[0:])
print(course[:])

# def calc_age(date):
#     return 2023 - date
#
#
#
# birth_date=int(input("Enter your Birth date "))
# print(calc_age(birth_date))
