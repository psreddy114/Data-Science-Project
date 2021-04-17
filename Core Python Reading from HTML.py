#!/usr/bin/env python
# coding: utf-8

# # Reading the html file in python

# In[10]:


import pandas as pd
from pandas import read_html
import html5lib


# In[23]:


url = "https://www.moneycontrol.com/mutual-funds/performance-tracker/returns/multi-cap-fund.html"


# In[24]:


tables_list = pd.io.html.read_html(url)


# In[25]:


tables_list


# In[28]:


mf_list = tables_list[0]


# In[29]:


mf_list


# In[40]:


10^-6


# In[52]:


List = [0,1,2,3,[4,5,6],5,6,7,8,9]


# In[70]:


List[4].index(6)


# In[72]:


# Sum of range in list
Rangetotal = list(range(1,9))
print(Rangetotal)


# In[81]:


Rangetotal1 = 1
for i in range(1,9):
    Rangetotal1 += i
print(Rangetotal1)


# In[80]:




