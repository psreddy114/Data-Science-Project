#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Numpy is a Python Library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transfrom and algebra.
# Numpy is created by Travis Oliphant in 2005. It is open source project anyone can use it freely.
# Numpy stands for Numerical Python.


# In[2]:


# In Python we have lists that serves the purpose of arrays, but they are slow to process.
import numpy as np 


# In[9]:


import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)


# In[10]:


import numpy as np
arr=numpy.array([1,2,3,4,5])
print(arr)


# In[11]:


import numpy as kelly
arr1=kelly.array([51,2,3,4,5])
print(arr1)


# In[12]:


import numpy as np
arr= numpy.array([1,2,3,4])
print(arr)


# In[14]:


# Checking NumPy Version
# The version string is stored under __version__ attribute.

# Example
import numpy as np

print(np.__version__)


# In[15]:


# NumPy Creating Arrays
# Create a NumPy ndarray Object
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.

# We can create a NumPy ndarray object by using the array() function.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr)) # type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.ndarray type.


# In[18]:


import numpy as np

list = np.array([1,2,3,4,5,6,7,8,9])

print(list)

print(type(list))


# In[20]:


# Use a tuple to create a NumPy array:

import numpy as np

tuple = np.array((1,2,3))

print(tuple)

print(type(tuple))


# In[22]:


# 0-D Arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

# Example
# Create a 0-D array with value 42

import numpy as np

arr = np.array(42)

print(arr)


# In[23]:


# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

# These are the most common and basic arrays.

# Example
# Create a 1-D array containing the values 1,2,3,4,5:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)


# In[24]:


# 2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.

# These are often used to represent matrix or 2nd order tensors.

# NumPy has a whole sub module dedicated towards matrix operations called numpy.mat

# Example
# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)


# In[25]:


import numpy as np
data = np.array(['a','b','c','d'])
print(data)


# In[26]:


# 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.

# These are often used to represent a 3rd order tensor.

# Example
# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)


# In[28]:


# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

# Example
# Check how many dimensions the arrays have:

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# In[29]:


# Higher Dimensional Arrays
# An array can have any number of dimensions.

# When the array is created, you can define the number of dimensions by using the ndmin argument.

# Example
# Create an array with 5 dimensions and verify that it has 5 dimensions:

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=4)

print(arr)
print('number of dimensions :', arr.ndim)


# In[32]:


# Access Array Elements
# Array indexing is the same as accessing an array element.

# You can access an array element by referring to its index number.

# The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

# Example
# Get the first element from the following array:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[3])
#print(arr[3])


# In[33]:


# Access 3-D Arrays
# To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.

# Example
# Access the third element of the second array of the first array:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])


# In[64]:


# To Generate Random Number
# NumPy offers the random module to work with random numbers.

# Example
# Generate a random integer from 0 to 100:

from numpy import random

x = random.randint(100)

print(x)


# In[92]:


# Generate Random Float
# The random module's rand() method returns a random float between 0 and 1.

# Example
# Generate a random float from 0 to 1:

from numpy import random

x = random.rand()

print(x)


# In[101]:


from numpy import random
random.rand()


# In[103]:


# Generate Random Array
# In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.

# Integers
# The randint() method takes a size parameter where you can specify the shape of an array.

# Example
# Generate a 1-D array containing 5 random integers from 0 to 100:

from numpy import random

x=random.randint(100, size=(5))

print(x)


# In[107]:


from numpy import random

x = random.randint(100, size=(6))

print(x)


# In[111]:


# Example
# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

from numpy import random

x = random.randint(100, size=(3,5))

print(x)


# In[119]:


# Floats  # pls fix this error
# The rand() method also allows you to specify the shape of the array.

# Example
# Generate a 1-D array containing 5 random floats:
from matplotlib import pyplot as plt 
from numpy import random

x = random.rand(5)
y= random.rand(5)

plt.bar(x,y)

print(x)
print(y)


# In[120]:


print(x)


# In[121]:


print(y)


# In[135]:


# Generate Random Number From Array
# The choice() method allows you to generate a random value based on an array of values.

# The choice() method takes an array as a parameter and randomly returns one of the values.

# Example
# Return one of the values in an array:

from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)


# In[143]:


# Example
# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):

from numpy import random

x = random.choice([3,5,7,9],size=[3,5])

print(x)


# In[144]:


# What is Vectorization?
# Converting iterative statements into a vector based operation is called vectorization.

# It is faster as modern CPUs are optimized for such operations.

# Add the Elements of Two Lists
# list 1: [1, 2, 3, 4]

# list 2: [4, 5, 6, 7]

# One way of doing it is to iterate over both of the lists and then sum each elements.


# In[152]:


# Example
# Without ufunc, we can use Python's built-in zip() method:

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)


# In[161]:


import numpy as np

s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
zip(s1, s2)
[(1, 'c'), (2, 'a'), (3, 'b')]


# In[179]:


# NumPy has a ufunc for this, called add(x, y) that will produce the same result.

# Example
# With ufunc, we can use the add() function:

import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)


# In[166]:


import numpy as np

x = [1, 2, 3, 4]
y = ["a", "b", "c", "d"]
z1 = (x, y)
[(1,"a"),(2,"b"),(3,"c"),(4,"d")]


# In[177]:


import numpy as np

x = [1, 2, 3, 4]
y = ["a", "b", "c", "d"]
z1 = np.add(x, y)

print(zipped)


# In[172]:


integers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped = zip(integers, letters, floats)  # Three input iterables
list(zipped)


# In[180]:


# Example
# Create your own ufunc for addition:

import numpy as np

def myadd2(x, y):
  return x+y

myadd2 = np.frompyfunc(myadd2, 2, 1)

print(myadd2([1, 2, 3, 4], [5, 6, 7, 8]))


# In[191]:


import numpy as np

def ufunction(a,b,c):
    return a+b+c

ufunction = np.frompyfunc(ufunction,3,1)

print(ufunction([1,2,3,4],[5,6,7,8],[9,10,11,12]))


# In[192]:


# Example
# Add the values in arr1 to the values in arr2:

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)


# In[209]:


# Subtraction
# The subtract() function subtracts the values from one array with the values from another array, and return the results in a new array.

# Example
# Subtract the values in arr2 from the values in arr1:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr)


# In[210]:


# Multiplication
# The multiply() function multiplies the values from one array with the values from another array, and return the results in a new array.

# Example
# Multiply the values in arr1 with the values in arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)


# In[211]:


# Division
# The divide() function divides the values from one array with the values from another array, and return the results in a new array.

# Example
# Divide the values in arr1 with the values in arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)


# In[212]:


# Power
# The power() function rises the values from the first array to the power of the values of the second array, and return the results in a new array.

# Example
# Raise the valules in arr1 to the power of values in arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)


# In[213]:


# Remainder
# Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, and return the results in a new array.

# Example
# Return the remainders:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)

print(newarr)


# In[225]:


import numpy as np

a = np.array([1,2,3,4])
b = np.array([1,2,3,4])

c = np.multiply(a,b)
print(c)


# In[226]:


# Truncation
# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.

# Example
# Truncate elements of following array:

import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr)


# In[227]:


# Example
# Same example, using fix():

import numpy as np

arr = np.fix([-3.1666, 3.6667])

print(arr)


# In[228]:


# Rounding
# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

# E.g. round off to 1 decimal point, 3.16666 is 3.2

# Example
# Round off 3.1666 to 2 decimal places:

import numpy as np

arr = np.around(3.1666, 2)

print(arr)


# In[229]:


# Example
# Find log at base 2 of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))


# In[237]:


x=2
print(np.log(x))


# In[238]:


# Log at Base 10
# Use the log10() function to perform log at the base 10.

# Example
# Find log at base 10 of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr))


# In[239]:


# Natural Log, or Log at Base e
# Use the log() function to perform log at the base e.

# Example
# Find log at base e of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print(np.log(arr))


# In[240]:


# Natural Log, or Log at Base e
# Use the log() function to perform log at the base e.

# Example
# Find log at base e of all elements of following array:

import numpy as np

arr = np.arange(1, 10)

print(np.log(arr))


# In[249]:


import math

print(math.cot(9))

