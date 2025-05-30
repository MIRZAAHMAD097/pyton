#1

side = float(input("Enter the side length of the square: "))
perimeter = 4 * side
area = side ** 2
print(f"Perimeter: {perimeter}")
print(f"Area: {area}")

#2

import math

diameter = float(input("Enter the diameter of the circle: "))
circumference = math.pi * diameter
print(f"Circumference: {circumference:.2f}")

#3

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
mean = (a + b) / 2
print(f"Mean: {mean}")


#4

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

sum_ab = a + b
product = a * b
square_a = a ** 2
square_b = b ** 2

print(f"Sum: {sum_ab}")
print(f"Product: {product}")
print(f"Square of {a}: {square_a}")
print(f"Square of {b}: {square_b}")
