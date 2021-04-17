#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = 5 
f = 1  
for x in range(1, n+1):  f = f * x
print(f)


# In[2]:


List = [1,52,6,4,8,9,5]


# In[4]:


List.reverse()
List


# In[5]:


print(ord('b')-ord('a'))


# In[22]:


print("D",end='')
print("C",end='')


# In[24]:


x = 3.3456789
'%f!%e!%g'%(x,x,x)


# In[27]:


x = 34
print("%f"%x)


# In[2]:


x = 'abcd'
for i in range(len(x)):
    x = "z"
    print(x)


# In[29]:


a = {"a":1}
b = dict(zip(a.values(),a.keys()))
b


# In[5]:


x = ("apple","banana","mango","cherry")
y = list(x)
y[0] = "Orange"
x = tuple(y)

print(x)

