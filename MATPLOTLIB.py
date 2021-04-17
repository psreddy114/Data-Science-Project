#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[11]:


xpoints = np.array([0,6])
ypoints = np.array([0,250])


# In[4]:


plt.plot(xpoints, ypoints)
plt.show()


# In[9]:


import matplotlib.pyplot as plt
import numpy as np


# In[6]:


xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints, ypoints)
plt.show()


# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[33]:


# Draw two points in a diagram one at (1,3) and other at (8,10)

xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints, ypoints,'o')

plt.show()


# In[24]:


# Multiple Points

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,6,8])
y = np.array([3,8,1,10])

plt.plot(x,y)

plt.show()


# In[26]:


# Default X points

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ypoints = np.array([3,8,1,10,5,7])

plt.plot(ypoints)

plt.show()


# In[34]:


# Markers

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10,5,7,4,2,6,9])

plt.plot(ypoints, marker = 'o')

plt.show()


# In[2]:


# Format strings (fmt)
# Mark each point with a circle

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,5,7])

plt.plot(ypoints, 'o-.r')

plt.show()


# In[31]:


# Marker Size
# We can use keyword argument markersize or shorter version, ms to set the size of the markers.

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints, marker = 'o', ms = 20)

plt.show()


# In[1]:


# Marker Color
# We can use keyword argument markeredgecolor or the shorter verion, mec to set the colors of the edge of the markers

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ypoints = np.array([5,1,8,3,4,9])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')


# In[22]:


# Keyword argument for Markerfacecolor or the shorter version, mfc to set the color inside the edge of the markers:

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = '#FFA500', mfc = '#FF4500' )


# In[32]:


# Matplotlib Line
# Linestyle
# We can use keyword argument linestyle, or shorter version, ls to chang the style of the plotted line.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ypoints = np.array([5,7,9,1,3])

plt.plot(ypoints, linestyle = '-')

plt.show()


# In[39]:


# Line Color 
# Keyword argument color or shorter version, c to set the color of the line.

import matplotlib.pyplot as plt
import numpy as np

ypoints = ([5,8,6,1,7,3,9,5])

plt.plot(ypoints, marker = 'o', ms=20, mec='y',mfc = 'k', c='r')


# In[40]:


# Line width
# Keyword argument linewidth or shorter version, lw to change the width of the line.

# Line Color 
# Keyword argument color or shorter version, c to set the color of the line.

import matplotlib.pyplot as plt
import numpy as np

ypoints = ([5,8,6,1,7,3,9,5])

plt.plot(ypoints, marker = 'o', ms=20, mec='y',mfc = 'k', c='r', lw = 10)


# In[45]:


# Multiple Lines
# We can plot as many as line by adding more plt.plot() functions.

# Line width
# Keyword argument linewidth or shorter version, lw to change the width of the line.

# Line Color 
# Keyword argument color or shorter version, c to set the color of the line.

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([2,4,6,8,10,12,14,16])
y1 = np.array([5,8,6,1,7,3,9,5])
x2 = np.array([1,2,3,4,5,6,7,8])
y2 = np.array([4,8,1,9,3,8,9,2])

plt.plot(x1,y1)
plt.plot(x2,y2)

plt.show()


# In[49]:


# matplotlib Labels and Title
# Create Labels for a plot,by using xlabel() and ylabel() functions to set a label for the x and y axis.

# Creating a title, by using title() function set a title for the plot.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,10,15,20,25,30,35,40,45,50])
y = np.array([100,110,120,130,140,150,160,170,180,190])

plt.plot(x, y)

plt.title("Creating Title")
plt.xlabel("XLabel Header")
plt.ylabel("YLabel Header")

plt.show()


# In[54]:


# Setting Font properties to Title and Labels.
# By useing fontdict() function we can set the font properties to Titles and Labels.


import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,10,15,20,25,30,35,40,45,50])
y = np.array([100,110,120,130,140,150,160,170,180,190])

font1 = {'family':'arial', 'color':'yellow','size':20}
font2 = {'family':'arial', 'color':'magenta','size':15}
font3 = {'family':'arial', 'color':'#9ACD32','size':15}

plt.title("Creating Title", fontdict = font1)
plt.xlabel("XLabel Header", fontdict = font2)
plt.ylabel("YLabel Header", fontdict = font3)

plt.plot(x, y)

plt.show()


# In[58]:


# Position the Title
# By using loc parameter in title() function to position the title.
# Legal values are: 'left', 'right', and 'center'. Default value is 'center'.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,10,15,20,25,30,35,40,45,50])
y = np.array([100,110,120,130,140,150,160,170,180,190])

font1 = {'family':'arial', 'color':'yellow','size':20}
font2 = {'family':'arial', 'color':'magenta','size':15}
font3 = {'family':'arial', 'color':'#9ACD32','size':15}

plt.title("Creating Title", loc = 'center', fontdict = font1)
plt.xlabel("XLabel Header", fontdict = font2)
plt.ylabel("YLabel Header", fontdict = font3)

plt.plot(x, y)

plt.show()


# In[59]:


# Matplotlib Adding grid Lines,
# By using grid() function we can add grid lines to the plot.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,10,15,20,25,30,35,40,45,50])
y = np.array([100,110,120,130,140,150,160,170,180,190])

font1 = {'family':'arial', 'color':'yellow','size':20}
font2 = {'family':'arial', 'color':'magenta','size':15}
font3 = {'family':'arial', 'color':'#9ACD32','size':15}

plt.title("Creating Title", loc = 'center', fontdict = font1)
plt.xlabel("XLabel Header", fontdict = font2)
plt.ylabel("YLabel Header", fontdict = font3)

plt.plot(x, y)

plt.grid()
plt.show()


# In[62]:


# Specify which grid lines to be added to plot.
# By using axis parameter in the grid() function to specify which grid lines to display. 

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,10,15,20,25,30,35,40,45,50])
y = np.array([100,110,120,130,140,150,160,170,180,190])

font1 = {'family':'arial', 'color':'yellow','size':20}
font2 = {'family':'arial', 'color':'magenta','size':15}
font3 = {'family':'arial', 'color':'#9ACD32','size':15}

plt.title("Creating Title", loc = 'center', fontdict = font1)
plt.xlabel("XLabel Header", fontdict = font2)
plt.ylabel("YLabel Header", fontdict = font3)

plt.plot(x, y)

plt.grid(axis = 'y')

plt.show()


# In[70]:


# Setting the line properties for the grid.


import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,10,15,20,25,30,35,40,45,50])
y = np.array([100,110,120,130,140,150,160,170,180,190])

font1 = {'family':'arial', 'color':'yellow','size':20}
font2 = {'family':'arial', 'color':'magenta','size':15}
font3 = {'family':'arial', 'color':'#9ACD32','size':15}

plt.title("Creating Title", loc = 'center', fontdict = font1)
plt.xlabel("XLabel Header", fontdict = font2)
plt.ylabel("YLabel Header", fontdict = font3)

plt.plot(x, y)

plt.grid(axis = 'both', color = 'darkred', ls = ':', lw = 2)

plt.show()


# In[8]:


# Matplotlib Subplots
# With subplots() function you can draw multiple plots in one figure.

# Example: Draw two plots in single row and two columns.

import matplotlib.pyplot as plt
import numpy as np

# Plot1

x = np.array([1,5,8,4,6])
y = np.array([0,3,5,7,9])

plt.subplot(1,2,1)
plt.plot(x,y)

# Plot 2


x = np.array([0,1,2,3,4])
y = np.array([20,10,50,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()


# In[11]:


# Example: Draw two plots on top of each other (Two rows, one column)

import matplotlib.pyplot as plt
import numpy as np

# Plot1

x = np.array([1,5,8,4,6])
y = np.array([0,3,5,7,9])

plt.subplot(2,1,1)
plt.plot(x,y)

# Plot 2


x = np.array([0,1,2,3,4])
y = np.array([20,10,50,30,40])

plt.subplot(2,1,2)
plt.plot(x,y)


plt.show()


# In[12]:


# Example: Draw six plots in single row

import matplotlib.pyplot as plt
import numpy as np


# Plot1

x = np.array([1,5,8,4,6])
y = np.array([0,3,5,7,9])

plt.subplot(3,2,1)
plt.plot(x,y)

# Plot 2


x = np.array([0,1,2,3,4])
y = np.array([20,10,50,30,40])

plt.subplot(3,2,2)
plt.plot(x,y)

# Plot 3

x = np.array([2,5,3,4,6])
y = np.array([3,5,7,9,1])

plt.subplot(3,2,3)
plt.plot(x,y)

# Plot 4

x = np.array([5,4,1,3,3])
y = np.array([20,10,20,50,40])

plt.subplot(3,2,4)
plt.plot(x,y)

# Plot 5

x = np.array([2,5,1,3,6])
y = np.array([3,1,7,8,10])

plt.subplot(3,2,5)
plt.plot(x,y)

# Plot 6

x = np.array([5,4,1,3,3])
y = np.array([30,10,50,20,40])

plt.subplot(3,2,6)
plt.plot(x,y)

plt.show()


# In[4]:


# Example: Draw six plots in single figure, adding title to each plot.

import matplotlib.pyplot as plt
import numpy as np


# Plot1

x = np.array([1,5,8,4,6])
y = np.array([0,3,5,7,9])


plt.subplot(3,2,1)
plt.plot(x,y)
plt.title("SALES")

# Plot 2


x = np.array([0,1,2,3,4])
y = np.array([20,10,50,30,40])

plt.subplot(3,2,2)
plt.plot(x,y)
plt.title("PROFIT")

# Plot 3

x = np.array([2,5,3,4,6])
y = np.array([3,5,7,9,1])

plt.subplot(3,2,3)
plt.plot(x,y)
plt.title("DISCOUNT")

# Plot 4

x = np.array([5,4,1,3,3])
y = np.array([20,10,20,50,40])

plt.subplot(3,2,4)
plt.plot(x,y)
plt.title("INCOME")

# Plot 5

x = np.array([2,5,1,3,6])
y = np.array([3,1,7,8,10])

plt.subplot(3,2,5)
plt.plot(x,y)
plt.title("PERCENTAGE")

# Plot 6

x = np.array([5,4,1,3,3])
y = np.array([30,10,50,20,40])

plt.subplot(3,2,6)
plt.plot(x,y)
plt.title("INCOME 2")

plt.show()


# In[7]:


# Super TItle

import matplotlib.pyplot as plt
import numpy as np


# Plot1

x = np.array([1,5,8,4,6])
y = np.array([0,3,5,7,9])


plt.subplot(3,2,1)
plt.plot(x,y)
plt.title("SALES")

# Plot 2


x = np.array([0,1,2,3,4])
y = np.array([20,10,50,30,40])

plt.subplot(3,2,2)
plt.plot(x,y)
plt.title("PROFIT")

# Plot 3

x = np.array([2,5,3,4,6])
y = np.array([3,5,7,9,1])

plt.subplot(3,2,3)
plt.plot(x,y)
plt.title("DISCOUNT")

# Plot 4

x = np.array([5,4,1,3,3])
y = np.array([20,10,20,50,40])

plt.subplot(3,2,4)
plt.plot(x,y)
plt.title("INCOME")

# Plot 5

x = np.array([2,5,1,3,6])
y = np.array([3,1,7,8,10])

plt.subplot(3,2,5)
plt.plot(x,y)
plt.title("PERCENTAGE")

# Plot 6

x = np.array([5,4,1,3,3])
y = np.array([30,10,50,20,40])

plt.subplot(3,2,6)
plt.plot(x,y)
plt.title("INCOME 2")

plt.suptitle("SUPER TITLE")
plt.show()


# In[11]:


# Creater Scatter Plot

#We can draw scatter plot by using scatter() function.

import matplotlib.pyplot as plt
import numpy as np

x = ([6,1,9,5,1,7,5,3,8,5,2,6,5,4,9,1,8,3,7,2])
y = ([25,75,56,47,96,18,39,16,86,13,84,72,34,81,71,69,19,43,69,14])

plt.scatter(x,y)
plt.show()


# In[13]:


# Compare plots

import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars.

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y)

# day two, the age and speed of 15 cars.
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.scatter(x,y)

#day three, the age and speed of 20 cars.

x = ([6,1,9,5,1,7,5,3,8,5,2,6,5,4,9,1,8,3,7,2])
y = ([25,75,56,47,96,18,39,16,86,13,84,72,34,81,71,69,19,43,69,14])

plt.scatter(x,y)

plt.show()


# In[15]:


# By using color or c argument we can set own color to  each scatter plot.

import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars.

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y, color = 'red')

# day two, the age and speed of 15 cars.
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.scatter(x,y, color = 'orange')

plt.show()


# In[30]:


# By using array of color or c argument we can set specific color to  each dot in scatter plot.

import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars.

x = ([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = ([99,86,87,88,111,86,103,87,94,78,77,85,86])

dotcolors = (["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x,y, color=dotcolors)

plt.show()


# In[40]:


# Color Map

# You can specify the colormap with the keyword argument cmap with the value of the colormap, 
# in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.
# In addition you have to create an array with values (from 0 to 100), 
# one value for each of the point in the scatter plot:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()


# In[46]:


# Size, by using size we can change the sizez of the dot in scatter plot.

import matplotlib.pyplot
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x,y, s=sizes)

plt.show()


# In[47]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, c=colors, cmap='viridis', s=sizes)

plt.colorbar()

plt.show()


# In[48]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, c=colors, cmap='viridis', s=sizes, alpha = 0.25)

plt.colorbar()

plt.show()


# In[55]:


# Color map drawing by including the plt.colorbar() statement.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='ocean')

plt.colorbar()

plt.show()


# In[65]:


# Combine color size and Alpha

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(25))
y = np.random.randint(100, size=(25))

plt.scatter(x, y)


plt.show()


# In[69]:


import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='inferno')

plt.colorbar()

plt.show()


# In[73]:


# Creating Bars
# By using bar() function we draw bar graphs.

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A','B','C','D'])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()


# In[81]:


# Creating Bar Graph

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2,5,8,6,4,7,3,1])
y = np.array([100,85,64,53,48,28,39,76])

plt.bar(x,y)

plt.show()


# In[83]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Apples","Bananas","Oranges","Grapes"])
y = np.array([985,762,864,245])

plt.bar(x,y)

plt.show()


# In[84]:


# Creating Horinzontal Bars by using barh() function.

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Apples","Bananas","Oranges","Grapes"])
y = np.array([985,762,864,245])

plt.barh(x,y)

plt.show()


# In[89]:


# Creating bar() and  barh() Graph color by using argument 'color'.

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Apples","Bananas","Oranges","Grapes"])
y = np.array([985,762,864,245])

plt.bar(x,y, color='red')

plt.show()


# In[91]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Apples","Bananas","Oranges","Grapes"])
y = np.array([985,762,864,245])

plt.barh(x,y, color='red')

plt.show()


# In[93]:


# bar width takes the keyword argument width() to set the width of the bars.

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Apples","Bananas","Oranges","Grapes"])
y = np.array([985,762,864,245])

plt.bar(x,y, color='red',width = 0.25)

plt.show()


# In[97]:


# bar graph with width() argument.

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Apples","Bananas","Oranges","Grapes"])
y = np.array([985,762,864,245])

plt.bar(x,y, color='red',width = 0.80) # Default width value of bar is 0.80

plt.show()


# In[104]:


# barh graph with height() argument.

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Apples","Bananas","Oranges","Grapes"])
y = np.array([985,762,864,245])

plt.barh(x,y, color='red',height=0.25) # Default height value is 0.80

plt.show()


# In[105]:


# Create an histogram

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(150,25,250)

plt.hist(x)

plt.show()


# In[113]:


import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(5.0,1.0,100000)

plt.hist(x,100)

plt.show()


# In[116]:


# Create Pie chart by using pie() function.

import matplotlib.pyplot as plt
import numpy as np

y = np.array([55,25,15,45,5])

plt.pie(y)
plt.show()


# In[124]:


# Add label to the pie chart by using argument 'label'.

import matplotlib.pyplot as plt
import numpy as np

y = np.array([55,25,15,45,5])

labels = ["Apples","Bananas","Cherries","Dates","Orange"]

plt.pie(y, labels=labels)
plt.show()


# In[129]:


# Change the start Angle by using the keyword argument 'startangle'.

import matplotlib.pyplot as plt
import numpy as np

y = np.array([55,25,15,45,5])

labels = ["Apples","Bananas","Cherries","Dates","Orange"]

plt.pie(y, labels=labels, startangle=0)
plt.show()


# In[135]:


# Explode
# By using keyword argument 'explode'
# The explode parameter, if specified, and not None, must be an array with one value for each wedge.
#Each value represents how far from the center each wedge is displayed:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([55,25,15,45,5])

labels = ["Apples","Bananas","Cherries","Dates","Orange"]
explode = [0.2,0.18,0.16,0.14,0.12]

plt.pie(y, labels=labels, startangle=0, explode = explode)
plt.show()


# In[136]:


# Shadow
# Add a shadow to the pie chart by setting the shadows parameter to True:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([55,25,15,45,5])

labbels = ["Apples","Bananas","Cherries","Dates","Orange"]
explode = [0.2,0.18,0.16,0.14,0.12]

plt.pie(y, labels=labels, startangle=0, explode = explode, shadow = True)
plt.show()


# In[137]:


# Colors
# You can set the color of each wedge with the colors parameter.
# The colors parameter, if specified, must be an array with one value for each wedge:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([55,25,15,45,5])

labbels = ["Apples","Bananas","Cherries","Dates","Orange"]
explode = [0.2,0.18,0.16,0.14,0.12]
colors = ["black", "red", "orange", "#4CAF50","yellow"]

plt.pie(y, labels=labels, startangle=0, explode = explode, colors = colors, shadow = True)
plt.show()


# In[138]:


# Creating a Legend to chart.
# To add a list of explanation for each wedge, use the legend() function:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([55,25,15,45,5])

labbels = ["Apples","Bananas","Cherries","Dates","Orange"]
explode = [0.2,0.18,0.16,0.14,0.12]
colors = ["black", "red", "orange", "#4CAF50","yellow"]

plt.pie(y, labels=labels, startangle=0, explode = explode, colors = colors, shadow = True)
plt.legend()

plt.show()


# In[161]:


# Adding Title to the Legend of a chart.
# To add a list of explanation for each wedge, use the legend() function:


import matplotlib.pyplot as plt
import numpy as np

y = np.array([55,25,15,45,5])

labbels = ["Apples","Bananas","Cherries","Dates","Orange"]
explode = [0.2,0.18,0.16,0.14,0.12]
colors = ["black", "red", "orange", "#4CAF50","yellow"]

plt.pie(y, labels=labels, startangle=0, explode = explode, colors = colors, shadow = True)
plt.legend(title = "Five Fruits Chart", loc = "center right")

plt.title("PIE CHART", loc = 'center')

plt.show()

