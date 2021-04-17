#!/usr/bin/env python
# coding: utf-8

# Simple Linear Regression Method in Python
# 
# Simple Linear Regression is a statistical method to find relationship between two continuous variables. Out of the two variables present, one is independent variable and the other is dependent variable. Statistical relationship is not accurate in determining relationship between two variables. For Example relationship between height and weight.
# 
# (Y = b0 + b1 * x)
# where,
# y is the dependent variable
# x is the independent variable
# b0 is the base value of the relationship
# b1 is the slope of the line explaining the relationship between y & x.
# 
# For instance y refers to how does a person's salary change with the years of experience that he has. So in that case salary would be the dependant variable and experience will be the independent variable and the base value will be the salary of a person, who has no experience. In our code exaple, we are going to work on such a dataset.
# 
# A company wants to establish a relationship between salary of its employees and the experience they have. We will try to find out correlation by using Simple Linear Regression.

# In[3]:


# Importing the Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


# Loding the dataset of salary details and experince

dataset = pd.read_csv('C:\\Users\\SHASHI\\OneDrive\\Desktop\\Python\\SimpleLinearRegression.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# In[24]:


# Splitting the dataset into the Training set and Testing set

from sklearn.model_selection import train_test_split


# In[25]:


train_x, test_x, train_y, test_y = train_test_split(x,y, test_size = 1/3, random_state = 0)


# After executing this code, we have our training and testing sets split along with arrays and vectors of independent and dependent attributes respectively.

# In[26]:


print(train.shape)
print(test.shape)
dataset.head()


# In[33]:


# Now fit the dataset into Simple Linear Regression Model

from sklearn.linear_model import LinearRegression # for Logistic Regression algorithm
regressor = LinearRegression()
regressor.fit(train_x, train_y)


# In[56]:


# Predicting the Test set results
Yprediction = regressor.predict(test_x)
print(Yprediction)


# In[52]:


# Predicting the Train set results
Yprediction = regressor.predict(train_x)
print(Yprediction)


# Visualising the correlation in the dataset
# 
# In order to judge the actual correlation amongst the data, we are going to plot two curves.
# 
# Visualising the Training set results
# 
# We do this using the following code:

# In[58]:


# Visualising the Training set results
plt.scatter(train_x, train_y, color = 'Red')
plt.plot(train_x, regressor.predict(train_x), color = 'green')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# The line we have here is not that bad, since only a few points lie very far from it, most of the points lie around the line itself.

# In[59]:


# Visualising the Testing set results
plt.scatter(test_x, test_y, color = 'Red')
plt.plot(test_x, regressor.predict(test_x), color = 'green')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# It shows that 5 out of 10 data points lie on the line itself. 3 out of 10 are very near to the line and only 2 are further to the line.
