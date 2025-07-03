#lesson 16
#1
import numpy as np

num_list = [12.23, 13.32, 100, 36.32]
print("original list: ", num_list)

array_1d = np.array(num_list)
print("1d numpy array: ", array_1d)

#2

import numpy as np

numbers = np.arange(2, 11)
matrix = numbers.reshape(3, 3)

print("3x3 matritsa: ")
print(matrix)

#3

import numpy as np

vector = np.zeros(10)
print("boshlang'ich null vector: ")
print(vector)

vector[5] = 11
print("\nO'zgartirilgan vector (6-element = 11): ")
print(vector)

#4

import numpy as np

array = np.arange(12, 38)
print(array)


#5

import numpy as np

array = np.array([1,2,3,4])

float_array = array.astype(float)

print("array: ", array)
print("float array: ", float_array)


#6

import numpy as np

centigrade = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])

fahrenheit = centigrade * 9 / 5 + 32

print("Values in Centigrade degrees:", centigrade)
print("Values in Fahrenheit degrees:", fahrenheit)

#7

import numpy as np

array1 = np.array([10,20,30])
print("arrar1: ", array1)

values_to_append = np.array([40,50,60,70,80,90])

appended_array = np.append(array1, values_to_append)
print("appended array: ", appended_array)

#8

import numpy as np

random_array = np.random.randint(1, 100, size=10)
print("random array: ", random_array)

mean = np.mean(random_array)
print("mean: ", mean)

median = np.median(random_array)
print("median: ", median)

std = np.std(random_array)
print("std: ", std)

#9

import numpy as np

random_array = np.random.rand(10, 10)

print("random 10x10 array: ")
print(random_array)

min_value = np.min(random_array)
max_value = np.max(random_array)

print("\nminimum value: ", min_value)
print("\nmaximum value: ", max_value)

#10

import numpy as np

array3d = np.random.rand(3, 3, 3 )

print("3x3x3 random value: ")
print(array3d)
