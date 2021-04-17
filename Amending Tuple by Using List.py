#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Amending tuple by using list function

x = ("a","b")
y = list(x)
y[1] = "Z"
x = tuple(y)

print(x)

