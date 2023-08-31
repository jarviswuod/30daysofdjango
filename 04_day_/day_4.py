# Modules
# Method 1
import converters

# Method 2
from converters import kg_to_lbs

print(kg_to_lbs(90))

print(converters.lbs_to_kg(70))

print('-------------------------------------------')
# CHALLENGE 1
from utils import find_max

numbers = [10, 3, 8, 2, 6, 8, 1]
max_value = find_max(numbers)
print(max_value)

print('-------------------------------------------')
# PACKAGES
# Method 1
import ecommerce.shipping

ecommerce.shipping.calc_shipping()

# Method 2
# Approach 1
from ecommerce.shipping import calc_shipping

print(calc_shipping())

# Approach 2
from ecommerce import shipping

print(shipping.calc_shipping())

print('-------------------------------------------')
# GENERATING RANDOM VALUES
import random

for i in range(3):
    print(random.random())

print('-------------------------------------------')
for i in range(3):
    print(random.randint(10, 20))

members = ['John', "Mary", 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)

print('-------------------------------------------')


# CHALLENGE 2

class Dice:
    def roll(self):
        val_1 = random.randint(1, 6)
        val_2 = random.randint(1, 6)
        return val_1, val_2


dice = Dice()
print(dice.roll())

print('-------------------------------------------')
# FILES AND DIRECTORIES
from pathlib import Path

# 1. Absolute path
# c:\Program Files\Microsoft
# /usr/local/bin

# 2. Relative path

print('-------------------------------------------')
path = Path('ecommerce')
print(path.exists())
path2 = Path('email')
# print(path2.mkdir())
# print(path2.rmdir())

print('-------------------------------------------')
path = Path()
# print(path.glob('*'))
# print(path.glob('*.py'))
for file in path.glob('*.py'):
    print(file)

print('-------------------------------------------')
for file in path.glob('*'):
    print(file)

print('-------------------------------------------')
# Pypi and Pip
