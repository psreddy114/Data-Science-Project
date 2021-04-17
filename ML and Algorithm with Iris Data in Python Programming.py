#!/usr/bin/env python
# coding: utf-8

# In[67]:


# Data Pre processing for Iris Data in Python
# Link: https://www.kaggle.com/ash316/ml-from-scratch-with-iris

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from subprocess import check_output


# In[68]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output


# In[146]:


# Load the dataset  Iris data in to Python

Iris = pd.read_csv("C:/Users/SHASHI/Downloads/Iris.csv")
Iris.head(5) # Show the first five rows of dataset


# In[147]:


# Checking the data set type to check if there is any inconsistences, as we can see there is no null values in the info we can process it.

Iris.info()


# In[149]:


# Removing the column not necessary in pre-processing.

Iris.drop('Id', axis=1, inplace=True)


# In[150]:


Iris.head(5)


# In[151]:


# Exploratory Data Analysis

fig = Iris[Iris.Species == 'setosa'].plot(kind='scatter',x='Sepal.Length',y='Sepal.Width',color='Red',label='setosa')
Iris[Iris.Species == 'versicolor'].plot(kind='scatter',x='Sepal.Length',y='Sepal.Width',color='Black',label='versicolor',ax = fig)
Iris[Iris.Species == 'virginica'].plot(kind='scatter',x='Sepal.Length',y='Sepal.Width',color='Yellow',label='virginica',ax=fig)
fig.set_xlabel("Sepal Length")
fig.set_ylabel("Sepal_Width")
fig.set_title("Sepal Length Vs Width")
fig=plt.gcf()
fig.set_size_inches(10,6)
plt.show()


# In[152]:


# Above graph show relationship between sepal length and width
Iris.head(3)


# In[153]:


# Below graph will show the relationship between Petal length and Width.

fig = Iris[Iris.Species == 'setosa'].plot(kind='scatter',x='Petal.Length',y='Petal.Width',color='Red',label='setosa')
Iris[Iris.Species == 'versicolor'].plot(kind='scatter',x='Petal.Length',y='Petal.Width',color='Black',label='versicolor',ax = fig)
Iris[Iris.Species == 'virginica'].plot(kind='scatter',x='Petal.Length',y='Petal.Width',color='Yellow',label='virginica',ax=fig)
fig.set_xlabel("Petal Length")
fig.set_ylabel("Petal_Width")
fig.set_title("Petal Length Vs Width")
fig=plt.gcf()
fig.set_size_inches(10,6)
plt.show()


# In[154]:


# Lets check how are the length and width are distributed.

Iris.hist(edgecolor='Red', linewidth=2)
fig=plt.gcf()
fig.set_size_inches(12,6)
plt.show()


# In[155]:


Iris.head(2)


# In[156]:


# How the length and width vary according to the species.

plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
sns.violinplot(x='Species',y='Petal.Length',data=Iris)
plt.subplot(2,2,2)
sns.violinplot(x='Species',y='Petal.Width',data=Iris)
plt.subplot(2,2,3)
sns.violinplot(x='Species',y='Sepal.Length',data=Iris)
plt.subplot(2,2,4)
sns.violinplot(x='Species',y='Sepal.Width',data=Iris)


# In[79]:


# The violinplot shows density of the length and width in the species. 
# The thinner part denotes that there is less density whereas the fatter part conveys higher density


# In[157]:


# Classification: samples belong to two or more classes and we want to learn from already labeled data,
# how to predict the class of unlabeled data

# Regression: if the desired output consists of one or more continuous variables, then the task is called regression. 
# An example of a regression problem would be the prediction of the length of a salmon as a function of its age and weight.

# attributes-->An attribute is a property of an instance that may be used to determine its classification. 
# In the following dataset, the attributes are the petal and sepal length and width. It is also known as Features.

# Target variable, in the machine learning context is the variable that is or should be the output. 
# Here the target variables are the 3 flower species.

from sklearn.linear_model import LogisticRegression # for Logisti Regression algorithm
from sklearn.model_selection import train_test_split # to split the dataset for training and testing
from sklearn.neighbors import KNeighborsClassifier # for K nearest neighbours
from sklearn import svm # for support Vector Machine SVM Algorithm
from sklearn import metrics # for checking the model accuracy
from sklearn.tree import DecisionTreeClassifier # for using Decision Tree Algorithm

print(Iris.shape)


# In[158]:


# Now, when we train any algorithm, the number of features and their correlation plays an important role. 
# If there are features and many of the features are highly correlated, then training an algorithm with all 
# the featues will reduce the accuracy. Thus features selection should be done carefully. 
# This dataset has less featues but still we will see the correlation.

plt.figure(figsize=(7,4))
sns.heatmap(Iris.corr(), annot=True, cmap='cubehelix_r') # draws heatmap with input as the correlation matrix calculated by Iris.corr().

plt.show()


# In[159]:


# Observation--->

# The Sepal Width and Length are not correlated The Petal Width and Length are highly correlated
# We will use all the features for training the algorithm and check the accuracy.
# Then we will use 1 Petal Feature and 1 Sepal Feature to check the accuracy of the algorithm 
# as we are using only 2 features that are not correlated. Thus we can have a variance in the dataset 
# which may help in better accuracy. We will check it later.


# Steps To Be followed When Applying an Algorithm
# 1. Split the dataset into training and testing dataset. 
#    The testing dataset is generally smaller than training one as it will help in training the model better.
# 2. Select any algorithm based on the problem (classification or regression) whatever you feel may be good.
# 3. Then pass the training dataset to the algorithm to train it. We use the .fit() method
# 4. Then pass the testing data to the trained algorithm to predict the outcome. We use the .predict() method.
# 5. We then check the accuracy by passing the predicted outcome and the actual output to the model.

# Splitting the Data into Training and Testing Dataset

train, test = train_test_split(Iris, test_size = 0.3) # In this main data is split into train and test
# the attribute test_size = 0.3 splits the data into 70% and 30% ratio. Train=70% and test = 30%

print(train.shape)
print(test.shape)

Iris.head(2)


# In[160]:


train_X = train[['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']] # taking the training data features
train_y = train.Species # output of our training data.

test_X = test[['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']] # taking the test data features
test_y = test.Species # output value of test data


# In[161]:


# Lest check the Train and Test Dataset.

train_X.head(2)


# In[162]:


test_X.head(2)


# In[163]:


test_y.head()


# In[164]:


train_y.head()


# In[165]:


# Support Vector Machine (SVM)

model = svm.SVC() # selecting the algorithm
model.fit(train_X, train_y) # we will train the algorithm with the training data and the training ouput.

prediction=model.predict(test_X) # now we pass the testing data to the trained algorithm
print('The accuracy of the SVM is:',metrics.accuracy_score(prediction,test_y)) # now we check the accuracy of the algorith.

# We pass the predicted output by the model and actual output


# In[166]:


# SVM has given 93% percent accuracy. We will continue to check the accuracy for different models.

#Logistic Regression Model Algorithm

model = LogisticRegression()
model.fit(train_X,train_y)
prediction=model.predict(test_X)
print('The accuracy of the Logistic Regression is:',metrics.accuracy_score(prediction,test_y))


# In[167]:


# Decision Tree Model of Algorithm

model = DecisionTreeClassifier()
model.fit(train_X,train_y)
prediction=model.predict(test_X)
print('The accuracy of the Decision Tree is:', metrics.accuracy_score(prediction,test_y))


# In[168]:


# K-Nearest Neighbours Model of Algorithm

model = KNeighborsClassifier(n_neighbors=3) # this examines 3 neighbours for putting the new data into a class

model.fit(train_X,train_y)
prediction=model.predict(test_X)
print('The accuracy of the KNN is:',metrics.accuracy_score(prediction,test_y))


# In[169]:


# Checking with various values of n for K-Nearest neibhors

a_index = list(range(1,11))
a = pd.Series()
x = [1,2,3,4,5,6,7,8,9,10]
for i in list(range(1,11)):
    model=KNeighborsClassifier(n_neighbors=i)
    model.fit(train_X,train_y)
    prediction=model.predict(test_X)
    a=a.append(pd.Series(metrics.accuracy_score(prediction,test_y)))
plt.plot(a_index,a)
plt.xticks(x)
Iris.head(1)


# In[170]:


# Creating Petals and Sepals Training Data

Petal = Iris[['Petal.Length','Petal.Width','Species']]
Sepal = Iris[['Sepal.Length','Sepal.Width','Species']]


# In[171]:


train_p, test_p = train_test_split(Petal,test_size=0.3,random_state=0) # Petals
train_x_p=train_p[['Petal.Length','Petal.Width']]
train_y_p=train_p.Species
test_x_p=test_p[['Petal.Length','Petal.Width']]
test_y_p=test_p.Species

train_s, test_s = train_test_split(Sepal,test_size=0.3,random_state=0) # Sepals
train_x_s=train_s[['Sepal.Length','Sepal.Width']]
train_y_s=train_s.Species
test_x_s=test_s[['Sepal.Length','Sepal.Width']]
test_y_s=test_s.Species


# In[172]:


# SVM

model = svm.SVC()
model.fit(train_x_p,train_y_p)
prediction=model.predict(test_x_p)
print('The accuracy of the SVM using Petals is:',metrics.accuracy_score(prediction,test_y_p))

model = svm.SVC()
model.fit(train_x_p,train_y_s)
prediction=model.predict(test_x_s)
print('The accuracy of the SVM using Sepal is:',metrics.accuracy_score(prediction,test_y_s))


# In[174]:


# Logistic Regression

model = LogisticRegression()
model.fit(train_x_p,train_y_p)
prediction=model.predict(test_x_p)
print('The accuracy of the Logistic Regression using Petals is:', metrics.accuracy_score(prediction,test_y_p))

model.fit(train_x_s,train_y_s)
prediction=model.predict(test_x_s)
print('The accuracy of the Logistic Regression using sepals is:',metrics.accuracy_score(prediction, test_y_s))


# In[176]:


# Decision Tree

model=DecisionTreeClassifier()
model.fit(train_x_p, train_y_p)
prediction=model.predict(test_x_p)
print('The accuracy of the Decision Tree using Petals is:', metrics.accuracy_score(prediction,test_y_p))

model.fit(train_x_s, train_y_s)
prediction=model.predict(test_x_s)
print('The accuracy of the Decision Tree using Sepals is:', metrics.accuracy_score(prediction,test_y_s))


# In[177]:


# K-Nearest Neighbuors

model=KNeighborsClassifier(n_neighbors=3)
model.fit(train_x_p,train_y_p)
prediction=model.predict(test_x_p)
print('The accuracy of the KNN using Petals is:', metrics.accuracy_score(prediction, test_y_p))

model.fit(train_x_s,train_y_s)
prediction=model.predict(test_x_s)
print('The accuracy of the KNN using Sepals is:', metrics.accuracy_score(prediction, test_y_s))

