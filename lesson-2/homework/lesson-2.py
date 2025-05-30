
#1
from datetime import datetime

name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
current_year = datetime.now().year
age = current_year - birth_year
print(f"Hello {name}, you are {age} years old.")

#2

txt = 'LMaasleitbtui'
car_name = ''.join(sorted(txt, key=lambda x: 'Mitsubishi'.find(x) if x in 'Mitsubishi' else 100))
print("Extracted car name:", car_name)

#3

txt = 'MsaatmiazD'
car_name = ''.join([ch for ch in txt if ch.lower() in 'mazda'])
print("Extracted car name:", car_name.capitalize())


#4

txt = "I'am John. I am from London"
import re
match = re.search(r'from (\w+)', txt)
if match:
    print("Residence Area:", match.group(1))
else:
    print("Residence not found.")

#5

user_input = input("Enter a string: ")
print("Reversed string:", user_input[::-1])

#6

text = input("Enter a string: ").lower()
vowels = 'aeiou'
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)


#7

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Maximum value:", max(numbers))


#8

word = input("Enter a word: ")
if word == word[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

#9

email = input("Enter your email: ")
domain = email.split('@')[-1]
print("Email domain:", domain)

#10

import random
import string

length = int(input("Enter desired password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(characters, k=length))
print("Generated password:", password)

