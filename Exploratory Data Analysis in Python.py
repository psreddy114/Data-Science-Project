#!/usr/bin/env python
# coding: utf-8

# In[2]:


1 # Importing Required libraries

import pandas as pd
import numpy as np
import seaborn as sns # Visualisation
import matplotlib.pyplot as plt # Visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[6]:


# 2. Loading the data in to the data frame, read the csv file in to data frame and pandas data frame.

df = pd.read_csv("C:/Users/SHASHI/OneDrive/Desktop/Python/EDA.csv")
df.head(5)


# In[8]:


df.tail(5)


# In[10]:


# 3. Checking the types of the data, we check the data types to understand and make or convert if any required 
# numeric data is been saved as strink or object.

df.info()


# In[17]:


df.dtypes


# In[19]:


# 4. Dropping irrelevant columns from the data.

# This step is certainly needed in every EDA because sometimes there would be many columns that we never use in such 
# cases dropping is the only solution. In this case, the columns such as Engine Fuel Type, Market Category, Vehicle style, 
# Popularity, Number of doors, Vehicle Size doesn't make any sense to me so I just dropped for this instance.

df = df.drop(['Engine Fuel Type','Market Category','Vehicle Style','Popularity','Number of Doors','Vehicle Size'],axis=1)
df.head(5)


# In[20]:


df.info()


# In[22]:


# Renaming the columns
# In this instance, most of the column names are very confusing to read, so I just tweaked their column names. 
# This is a good approach it improves the readability of the data set.

df = df.rename(columns={"Engine HP": "HP","Engine Cylinders": "Cylinders", "Transmission Type": "Transmission","Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price"})

df.head(5)


# In[23]:


# 6. Dropping the duplicate rows
# This is often a handy thing to do because a huge data set as in this case contains more than 10,000 rows 
# often have some duplicate data which might be disturbing, so here I remove all the duplicate value from the data-set. 
# for example prior to removing I had 11914 rows of data but after removing the duplicates 10925 data meaning 
# that I had 989 of duplicate data.

df.shape


# In[24]:


duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows:", duplicate_rows_df.shape)


# In[25]:


# Removing the duplicate values as this values are not necessary.

df.count() # Used to count the number of rows


# In[26]:


df = df.drop_duplicates()
df.head(5)


# In[27]:


df.count()


# In[29]:


# 7. Dropping the missing or Null Values from Dataset.

print(df.isnull().sum())


# In[30]:


df = df.dropna() # dropping the missing values.
df.count()


# In[31]:


print(df.isnull().sum()) # Rechecking for null values after dropping in data set.


# In[32]:


# 8. Detecting Outliers

# An outlier is a point or set of points that are different from other points. Sometimes they can be very high or very low.
# It's good to identify and remove them, because they results in less accuracy. 
# To remove outliers we are performing IQR score technique. Often outliers can be seen with visualizations using a box plot.
# Creating boxplot for all columns.

sns.boxplot(x=df['Price'])


# In[33]:


sns.boxplot(x=df['HP'])


# In[36]:


sns.boxplot(x=df['Cylinders'])


# In[37]:


Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3-Q1
print(IQR)


# In[38]:


df.describe()


# In[44]:


# Finding Outliers with below formual.

df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape


# In[46]:


# As we can see 1636 outliers been found from data set. Total count before outliers was 10,827. Now its been reduced to 
# 9191, difference of 1636 are outliers, which are removed now.


# In[49]:


# 9. Plot different features against one another (scatter), against frequency (histogram)

df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make')


# In[51]:


# Heat maps, is necessary when we need to find the dependent variables. Best way to find the releationship between the 
# features is by using heat maps. In the below map we know that price feature depends mainly on Engine size, HP, Cylinders.

plt.figure(figsize=(10,5))
c = df.corr()
sns.heatmap(c,cmap="BrBG", annot=True)
c


# In[52]:


# Scatterplot
# We generally use scatter plots to find the correlation between two variables. Here the scatter plots are plotted between
# Horsepower and Price and we can see the plot below, With the plot given below, we can easily draw a trend line.

fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()

