#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[12]:


import random
print(random.randrange(1,10))


# In[2]:


print("Hello, World!")


# In[3]:


# Python Indentation
if 5 > 2:
    print("Five is greater than two!")


# In[6]:


# Creating Python Variables
x = 5
y = "Hello, World"
print(x)
print(y)


# In[7]:


#This is a Comment
print("Hello, World!")


# In[8]:


x = 5
x = "PSR"
print(x)


# In[10]:


# Casting - Get the type() of function

x = "str"
y = 5

print(type(x))
print(type(y))


# In[11]:


# Single or Double Quotes

x = "John"
x = 'John'
print(x)


# In[12]:


# Case sensitive

a = 10
A = "PSR"
print(a)
print(A)


# In[13]:


# Variable Names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


# In[16]:


# Camel Case (Each word except first letter starts with Capital letter)
myVariableName = "John"

# Pascal Case (Each word starts with Capital letter)
MyVariableName = "John"

#Snake Case (Each word is seperated with underscore character)
my_variable_name = "John"


# In[19]:


#Many values to multiple variables
x,y,z = "orange","banana","cherry"
print(x)
print(y)
print(z)


# In[20]:


#One value to multiple variables
x=y=z = "orange"
print(x)
print(y)
print(z)


# In[21]:


# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# In[22]:


# Output Variables
x = "awesome"
print("Python is " + x)


# In[23]:


#Global Variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


# In[9]:


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# In[23]:


#Concatenation of variables in Python

x = "fantastic"

def myfunc():
    
    myfunc()

print("Python is "+ x)


# In[25]:


# Multiple Variables

var1 = var2 = var3 = "Orange"
print(var1)
print(var2)
print(var3)


# In[28]:


# Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


# In[29]:


# Data Types
x = "Hello, World!"
type(x)


# In[17]:


a = """"Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# In[5]:


x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 


# In[6]:


x = 20

#display x:
print(x)

#display the data type of x:
print(type(x)) 


# In[7]:


x = 20.5

#display x:
print(x)

#display the data type of x:
print(type(x)) 


# In[10]:


x = 1j

#display x:
print(x)

#display the data type of x:
print(type(x))


# In[4]:


x = ("shashidhar","reddy","peddolla")

print("My Name is "+x)


# In[6]:


x = "awesome"
print("Python is "+x)


# In[2]:


if 5 > 2:
    print("Five is greater than two")


# In[3]:


if 5 >2:
    print("Five is greater than two!")
if 5 < 7:
    print("Five is less than seven!")


# In[5]:


if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two")


# In[6]:


x = 5
y = "Hello World!"


# In[7]:


print(x)
print(y)


# In[8]:


print(type(x))
print(type(y))


# In[9]:


x,y,z = "orange","banana","apple"


# In[10]:


s = x,y,z


# In[11]:


print(s)


# In[13]:


print(x,y,z)


# In[14]:


print(x)
print(y)
print(z)


# In[16]:


x = "awesome"
print("Python is "+x )


# In[20]:


x = "awesome"
def myfunc(): # Create a variable outside of function, and use it inside the function
    print("Python is "+x)


# In[22]:


myfunc()


# In[25]:


x = "Python is a good programming tool"
def abc():
    print("Computer Language tool, "+x)


# In[26]:


abc()


# In[31]:


# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic" # here x is a local variable
  print("Python is " + x)

myfunc()   


# In[28]:


myfunc()


# In[33]:


print("Python is " + x) # here x is a global variable


# In[38]:


# Example: If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# In[39]:


# This is a comment
print("Hello World!")


# In[40]:


"""
This a comment
written in
more than just one line
"""
print("Hello World! How are you")


# In[63]:


x = "Hello World!"
print(type(x))
x = 20
print(type(x))
x = 20.5
print(type(x))
x = 1j
print(type(x))
x = ["apple","banana","orange"]
print(type(x))
x = ("apple","banana","orange")
print(type(x))
x = range(6)
print(type(x))
x = {"apple","banana","orange"}
print(type(x))
x = frozenset({"apple","banana","orange"})
print(type(x))
x = True
y = False
print(type(x))
print(type(y))
x = b"Hello"
print(type(x))
x = bytearray(10)
print(type(x))
x = memoryview(bytes(10))
print(type(x))


# In[64]:


byte_array = bytearray('XYZ', 'utf-8')
print('Before update:', byte_array)


# In[65]:


# Int: Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


# In[66]:


a = 10
b = 20

if b > 2:
    print("B is greater than a")
else:
    print("B is not greater than a")


# In[71]:


#Evaluate Values and Variables
#The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool(""))
print(bool(0))


# In[69]:


x = "Hello"
y = 15

print(bool(x))
print(bool(y))


# In[72]:


# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.
bool("abc")
bool(123)
bool(["apple","banana"])


# In[24]:


L = ["apple","banana","orange",1,2,3,4]


# In[25]:


L.insert(6,"mango")


# In[26]:


L


# In[27]:


L1 = ["grapes","tomato","potato"]


# In[28]:


L1.extend(L)


# In[29]:


L


# In[30]:


L1


# In[32]:


len(L1) # Gives the lenth of the elements in List


# In[33]:


L1.count(4) # Gives the count of element available in list


# In[41]:


L1.remove("banana")


# In[42]:


L3 = [9,5,3,6,4,7,1,8,2,3,4,5,8,9,1]


# In[43]:


L3.sort()


# In[44]:


L3


# In[46]:


L3.sort(reverse=True)


# In[47]:


L3


# In[48]:


L3.pop() # Pop deletes the last element from List


# In[49]:


L3


# In[52]:


L3.pop(5) # deletes the element at the position from the list


# In[60]:


del L3[6] # deletes all the element in range starting from index mentioned in arguments from the list


# In[61]:


L3


# In[63]:


L3.remove(5) # Deletes the particular element from the list


# In[64]:


L3


# In[65]:


# Creating a List
List = ['G','E','E','K','S','F',
        'O','R','G','E','E','K','S']
print("Intial List: ")
print(List)


# In[66]:


Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)


# In[68]:


List


# In[67]:


Sliced_List = List[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_List)


# In[69]:


List


# In[70]:


Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)


# In[74]:


# Negative index list slciing
print("Initial List: ")
print(List)


# In[72]:


List


# In[75]:


Sliced_List = List[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List)


# In[76]:


Sliced_List = List[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List)


# In[77]:


# Printing elements in reverse
# using Slice operation
Sliced_List = List[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List)


# In[78]:


List


# In[101]:


L3


# In[110]:


Slice = L3[::-1]
print(Slice)


# In[89]:


L3.append("test")


# In[95]:


L3


# In[111]:


# Change Item Value
# To change the value of a specific item, refer to the index number:
# Example
# Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# In[112]:


# Loop Through a List
# You can loop through the list items by using a for loop:

# Example
# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


# In[113]:


# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:

# Example
# Check if "apple" is present in the list:

thislist = [ "apple","banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# In[118]:


thislist = ["apple", "banana", "cherry"]
if "ORANGE" in thislist:
  print("Yes, 'apple' is in the fruits list")
elif
 print("No organe is not present in fruits list")


# In[119]:


# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# There are ways to make a copy, one way is to use the built-in List method copy().

# Example
# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# In[120]:


# Another way to make a copy is to use the built-in method list().

# Example
# Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# In[121]:


# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.

# One of the easiest ways are by using the + operator.

# Example
# Join two list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# In[122]:


# Example
# Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# In[130]:


# Example
# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)

print(list1)


# In[143]:


# The list() Constructor
# It is also possible to use the list() constructor to make a new list.

# Example
# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# In[144]:


# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

# Example
# Print i as long as i is less than 6:
# Print will terminate i as long as i is greater that or equal to 6:
i = 1
while i < 6:
  print(i)
  i += 1


# In[150]:


a = 10
while a < 40:
    print(a)
    a += 6


# In[153]:


# The break Statement
# With the break statement we can stop the loop even if the while condition is true:

# Example
# Exit the loop when i is 3:

i = 10
while i < 66:
  print(i)
  if i == 42:
    break
  i += 16


# In[155]:


# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

# Example
# Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# In[156]:


# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

# Example
# Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

