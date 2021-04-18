#!/usr/bin/env python
# coding: utf-8

# # Logistic Regression with Python

# Link: https://github.com/krishnaik06/EDA1/blob/master/EDA.ipynb
# 
# Wokring with Titanic Data set from Kaggle, link provided above. This is a very famous data set and very often is a student's first step in machine learning!. 
# 
# We will be trying to predict classification - survival or deceased. Let's begin our understanding of implementing Logistic Regression in Python for classification.
# 
# We will use a semi-cleaned version of the titanic data set, if you use the data set hosted directly on kaggle, you may need to do some additional cleaning not shown in this lecture notebook.

# # Import Libraries

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Loading the Dataset Titanic
# 

# In[6]:


titanic = pd.read_csv("C:\\Users\\SHASHI\\OneDrive\\Desktop\\Python\\titanic.csv")


# In[7]:


titanic.head()


# # Exploratory Data Analysis

# ## Missing Data

# Lets exploratory data analysis, start by checking out missing data
# 
# We can use seaborn to create simple heatmap to see where we are missing data

# In[11]:


titanic.isnull() # returns true if any missing values present in file


# In[16]:


titanic.info()


# In[13]:


titanic.isnull().sum() # returns sum of mising values with column names.


# In[14]:


sns.heatmap(titanic.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# Roughly 20 percent of the Age data is missing. The proportion of Age missing is likely small enough for reasonable replacement with some form of imputation. Looking at the Cabin column, it looks like we are just missing too much of that data to do something useful with at a basic level. We'll probably drop this later, or change it to another feature like "Cabin Known: 1 or 0"
# 
# Let's continue on by visualizing some more of the data! Check out the video for full explanations over these plots, this code is just to serve as reference.

# In[18]:


sns.set_style('whitegrid')
sns.countplot(x='Survived', data=titanic)


# In[19]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Sex', data = titanic, palette='RdBu_r')


# In[21]:


sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Pclass',data=titanic,palette='rainbow')


# In[22]:


sns.distplot(titanic['Age'].dropna(),kde=False,color='darkred',bins=40)


# In[23]:


titanic['Age'].hist(bins=30,color='darkred',alpha=0.3)


# In[24]:


sns.countplot(x='SibSp',data=titanic)


# In[26]:


titanic['Fare'].hist(color='green',bins=40,figsize=(8,4))


# ### Cufflinks for plots

# In[33]:


import cufflinks as cf
cf.go_offline()


# In[34]:


titanic['Fare'].iplot(kind='hist',bins=30,color='green')


# ### Data Cleaning

# We want to fill in missing age data instead of just dropping the missing age data rows. One way to do this is by filling in the mean age of all the passengers(imputation). However we can be smarter about this and check the average age by passenger class.

# In[37]:


plt.figure(figsize=(12,7))
sns.boxplot(x='Pclass',y='Age',data=titanic,palette='winter')


# In[42]:


def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]
    
    if pd.isnull(Age):
        
        if Pclass == 1:
            return 37
        
        elif Pclass == 2:
            return 29
        
        else:
            return 24
        
    else:
        return Age


# #### Now lets apply function

# In[43]:


titanic['Age'] = titanic[['Age','Pclass']].apply(impute_age, axis=1)


# Lets check the heat map again!

# In[56]:


sns.heatmap(titanic.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[75]:


titanic.isnull().sum()


# In[46]:


titanic.head(2)


# Lets drop the cabin column and the row in Embarked that is Nan.

# In[49]:


titanic.drop('Cabin',axis=1,inplace=True)


# In[50]:


titanic.head()


# In[51]:


titanic.dropna(inplace=True)


# ### Converting Categorical Features

# We need to convert categorical features to dummy variables using pandas otherwise our machine learning algorithm wont be able to directly take in those features as in puts.

# In[52]:


titanic.info()


# In[55]:


pd.get_dummies(titanic['Embarked'],drop_first=True).head()


# In[58]:


titanic.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)


# In[60]:


titanic.head()


# In[61]:


titanic = pd.concat([titanic,sex,embark],axis=1)


# In[62]:


titanic.head()


# Now the dataset is ready for our model!

# ## Building a Logistic Regression model

# Start by splitting our dataset into training set and testing set

# In[95]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# In[96]:


X = titanic.drop("Survived",axis=1)
Y = titanic["Survived"]


# In[134]:


X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.3, random_state=101)


# ## Training and Predicting

# In[133]:


logmodel = LogisticRegression()
logmodel.fit(X_train,Y_train)


# In[135]:


predictions = logmodel.predict(X_test)


# In[136]:


from sklearn.metrics import classification_report


# In[137]:


classification_report(Y_test,predictions)


# In[138]:


from sklearn.metrics import confusion_matrix


# In[140]:


accuracy = confusion_matrix(Y_test,predictions)
accuracy


# In[131]:


from sklearn. metrics import accuracy_score


# In[132]:


accuracy_score(Y_test,predictions)


# In[141]:


predictions


# ## Evaluation
# 
# We can check precision, recall, f1-score using classifiaction report!

# In[142]:


from sklearn.metrics import classification_report


# In[143]:


classification_report(Y_test,predictions)

