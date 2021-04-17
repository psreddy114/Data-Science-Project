#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# data structure .py

import pandas as pd
import numpy as np

series1 = pd.Series([1,2,3,4])
print("series1:\n{}\n".format(series1))


# In[ ]:


# data_structure.py
print("series1.values: {}\n".format(series1.values))
print("series1.index: {}\n".format(series1.index))


# In[ ]:


# Data structure.py
series2 = pd.Series([1,2,3,4,5],
                   index=['A','B','C','D','E'])
print("series2:\n{}\n".format(series2))
print("E is {}\n".format(series2["E"]))


# In[ ]:


# Data_structure.py
df1 = pd.DataFrame(np.arange(16).reshape(4,4))
print("df1:\n{}\n".format(df1))


# In[ ]:


# Data structure.py with column names for Data Frame.

df2 = pd.DataFrame(np.arange(16).reshape(4,4),
columns = ["columns1","columns2","columns3","columns4"],
index = ["A","B","C","D"])
print("df2:\n{}\n".format(df2))


# In[ ]:


# Data structure.py with column data directly to create a data frame.

df3 = pd.DataFrame({"Note":['A','B','C','D','E','F','G'],
                   "weekday": ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']})
print("df3:\n{}\n".format(df3))


# # Reading Excel Files.
# 
# # Install library:xlrd

# In[1]:


pip install xlrd


# In[2]:


import pandas as pd
import numpy as np

excelfile = pd.read_excel("C:/Users/SHASHI/OneDrive/Desktop/Python/OrdersDataSet.xlsx")


# In[ ]:


import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})


# In[3]:


# Data Pre-processing project.

import pandas as pd
import numpy as np

sf = pd.read_csv("C:/Users/SHASHI/OneDrive/Desktop/Python/Data.csv")
sf.head(3)


# In[ ]:


# In this file there is the un-wanted info is available,such as “info”, “z_address”, “zipcode”
# We keep “neighborhood” as a location variable, “zipid” and “zestimate”
# This is the price estimated by Zillow, we don’t want our model to be affected by this, so, we will drop them.


# In[5]:


sf.drop(sf.columns[[12,14,15]], axis=1, inplace=True)
sf.info()


# In[9]:


sf['zindexvalue'] = pd.to_numeric(sf['zindexvalue'])

sf.lastsolddate.min(), sf.lastsolddate.max()


# In[11]:


sf.describe()


# In[16]:


# Creating Histogram for each numeric value columns:

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
sf.hist(bins=50, figsize=(20,15))
plt.savefig("attribute_histogram_plots")
plt.show()


# In[23]:


#Creating Scatter plot by using Longitude and Latitude.
sf.plot(kind="scatter", x="longitude", y="latitude", alpha=0.2)
plt.savefig('map1.png')


# In[25]:


# Applying the color to the most expensive to the least expensive areas.

sf.plot(kind="scatter", x="longitude", y="latitude", alpha=0.5, figsize=(10,5),c="lastsoldprice", cmap=plt.get_cmap("jet"),colorbar=True, sharex=False)
plt.savefig('map2.png')

