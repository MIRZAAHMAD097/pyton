#lesson 11

#1

python -m venv myenv
myenv\Scripts\activate
source myenv/bin/activate
pip install numpy pandas requests
pip list
deactivate


#2


import math



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

#string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

import math_operations as mo
import string_utils as su

# Math operations
print("Add:", mo.add(5, 3))
print("Subtract:", mo.subtract(10, 4))
print("Multiply:", mo.multiply(2, 8))
print("Divide:", mo.divide(10, 2))
print("Divide by zero:", mo.divide(10, 0))

# String operations
print("Reverse string:", su.reverse_string("hello"))
print("Vowel count:", su.count_vowels("hello"))


#3

import math

def area(radius):
    return math.pi * radius * radius

def circumference(radius):
    return 2 * math.pi * radius

from geometry import circle

r = 5
print("Radius:", r)
print("Area:", circle.area(r))
print("Circumference:", circle.circumference(r))


import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius


def read_file(file_path):
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "file not found."


def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

from geometry import circle

print("Radius: 5")
print("Area:", circle.calculate_area(5))
print("Circumference:", circle.calculate_circumference(5))

print("Radius: 7")
print("Area:", circle.calculate_area(7))
print("Circumference:", circle.calculate_circumference(7))


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

from file_operations import file_reader, file_writer


file_writer.write_file("test.txt", "hello")


matn = file_reader.read_file("test.txt")
print(matn)  