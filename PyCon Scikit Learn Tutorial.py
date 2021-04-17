#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# What is Machine Learning:
# In this section we will begin to explore the basic principles of machine learning. Machine Learning is about 
# building programs with tunable parameters (typically an array of floating point values) that are adjusted automatically 
# so as to improve their behavior by adapting to previously seen data.

# Machine Learning can be considered a subfield of Artificial Intelligence since those algorithms can be seen as building 
# blocks to make computers learn to behave more intelligently by somehow generalizing rather that just storing and 
# retrieving data items like a database system would do.

# We'll take a look at two very simple machine learning tasks here. The first is a classification task: 
# the figure shows a collection of two-dimensional data, colored according to two different class labels. 
# A classification algorithm may be used to draw a dividing boundary between the two clusters of points:

# Start matplotlib inline mode, so figures will appear in the notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


# Import the example plot from the figures directory
from fig_code import plot_sgd_separator
plot_sgd_separator()


# In[ ]:


from fig_code import plot_linear_regression
plot_linear_regression()


# In[4]:


import numpy as np

# Generating a random array
X = np.random.random((3, 5))  # a 3 x 5 array

print(X)


# In[7]:


# Accessing elements

# get a single element
print (X[0, 0])

# get a row
print (X[1])

# get a column
print (X[:, 1])


# In[9]:


# Transposing an array
print (X.T)


# In[11]:


# Turning a row vector into a column vector
y = np.linspace(0, 12, 5)
print(y)

# make into a column vector
print (y[:, np.newaxis])


# In[12]:


# Scipy Sparse Matrices
# We won't make very much use of these in this tutorial, but sparse matrices are very nice in some situations. 
# For example, in some machine learning tasks, especially those associated with textual analysis, the data may be 
# mostly zeros. Storing all these zeros is very inefficient. We can create and manipulate sparse matrices as follows:

# Create a random array with a lot of zeros
X = np.random.random((10, 5))
print (X)


# In[13]:


X[X < 0.7] = 0
print(X)


# In[15]:


from scipy import sparse

# turn X into a csr (Compressed-Sparse-Row) matrix
X_csr = sparse.csr_matrix(X)
print(X_csr)


# In[17]:


# convert the sparse matrix to a dense array
print (X_csr.toarray())


# In[19]:


# Sparse matrices support linear algebra:
y = np.random.random(X_csr.shape[1])
z1 = X_csr.dot(y)
z2 = X.dot(y)
np.allclose(z1, z2)


# In[20]:


# The CSR representation can be very efficient for computations, but it is not as good for adding elements. 
# For that, the LIL (List-In-List) representation is better:


# In[22]:


# Create an empty LIL matrix and add some items
X_lil = sparse.lil_matrix((5, 5))

for i, j in np.random.randint(0, 5, (15, 2)):
    X_lil[i, j] = i + j

print (X_lil)
print (X_lil.toarray())


# In[24]:


X_csr = X_lil.tocsr()
print( X_csr)


# In[26]:


# Matplotlib

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np

# plotting a line

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x));


# In[27]:


# scatter-plot points

x = np.random.normal(size=500)
y = np.random.normal(size=500)
plt.scatter(x, y);


# In[28]:


# showing images
x = np.linspace(1, 12, 100)
y = x[:, np.newaxis]

im = y * np.sin(x) * np.cos(y)
print(im.shape)


# In[29]:


# imshow - note that origin is at the top-left!
plt.imshow(im);


# In[30]:


# Contour plot - note that origin here is at the bottom-left!
plt.contour(im);

