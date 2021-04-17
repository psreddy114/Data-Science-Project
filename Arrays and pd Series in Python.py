#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


pip install numpy


# In[3]:


import pandas as pd
import numpy as np


# In[5]:


list = [] # empty list and empty tuple etc....
print(list)


# PANDAS AND SERIES

# In[12]:


# Create an empty series
# import pandas library and aliaising as pd
import pandas
ps = pandas.Series()
print(ps)


# In[1]:


# Create an Empty Series
# import the pandas library and aliasing as pd
import pandas 
ps = pandas.Series()
print (ps)


# In[3]:


# Create a Series from ndarray
# If data is an ndarray, then index passed must be of the same length. If no index is passed, then by default index will be range(n) where n is array length, i.e., [0,1,2,3…. range(len(array))-1].

# Example 1
# Live Demo
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print (s)


# In[4]:


# Example 2
# Live Demo
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)


# In[8]:


import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[1,2,3,4])
print(s)


# In[9]:


import pandas as pd
import numpy as np
a = [5,9,7,7]
xyz = pd.Series(a)
print(xyz)


# In[11]:


import pandas as pd
import numpy as np
x = [1,2,3,4,5]
index = pd.Series(x,index = ['a','b','c','d','e'])
print(index)


# In[14]:


import pandas as pd
import numpy as np
a = {"x":1,"y":2,"z":3}
index = pd.Series(a,index=["x","z"])
print(index)


# In[15]:


data = {"Calories": [420,380,225],
       "Duration": [60,55,50]}
abc = pd.DataFrame(data)

print(abc)


# In[16]:


# Create a Series from Scalar
# If data is a scalar value, an index must be provided. The value will be repeated to match the length of index

# Live Demo
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
s = pd.Series(5, index=[0, 1, 2, 3])
print (s)


# In[17]:


# Accessing Data from Series with Position
# Data in the series can be accessed similar to that in an ndarray.

# Example 1
# Retrieve the first element. As we already know, the counting starts from zero for the array, which means the first element is stored at zeroth position and so on.

# Live Demo
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
#print (s[0])
print(s)


# In[18]:


# Retrieve Data Using Label (Index)
# A Series is like a fixed-size dict in that you can get and set values by index label.

# Example 1
# Retrieve a single element using index label value.

# Live Demo
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve a single element
print (s['d'])


# In[19]:


# Create an Empty DataFrame
# A basic DataFrame, which can be created is an Empty Dataframe.

# Example
# Live Demo
#import the pandas library and aliasing as pd
import pandas as pd
df = pd.DataFrame()
print (df)


# In[20]:


# Create a DataFrame from Lists
# The DataFrame can be created using a single list or a list of lists.

# Example 1
# Live Demo
import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df)


# In[22]:


mtcars = pd.read_csv("C:\\Users\\SHASHI\\OneDrive\\Desktop\\Python\\mtcars.csv")


# In[24]:


mtcars.head()


# In[25]:


mtcars.describe()


# In[17]:


import pandas as pd
import numpy as np
xl = pd.read_excel("C:\\Users\\SHASHI\\OneDrive\\Desktop\\OrdersDataSet.xlsx")


# In[16]:


import pandas as pd
import numpy as np
tf = pd.read_excel("C:\\Users\\SHASHI\\OneDrive\\Desktop\\Test.xlsx")

