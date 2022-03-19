#!/usr/bin/env python
# coding: utf-8

# # Practical Data Visualization
# ## Segment 3 - Plot formatting

# In[2]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from pylab import rcParams


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
rcParams['figure.figsize'] = 5, 4


# ### Defining plot color

# In[4]:


x = range(1,10)
y = [1,2,3,4,0.5,4,3,2,1]

plt.bar(x,y)


# In[13]:


wide = [.5,.5,.5,.7,.5,.7,.5,.5,.5]
color = ['salmon']
plt.bar(x,y, width = wide, color = color, align = 'center')


# In[5]:


address = 'mtcars.csv'

cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

df = cars[['cyl', 'mpg', 'wt']]
df.plot()


# In[15]:


color_theme = ['darkgray','lightsalmon','powderblue']
df.plot(color=color_theme)


# In[27]:


z = [7,8,.6,9,3,4,3,2,1,.5]
plt.pie(z)
plt.show()


# In[28]:


color_theme = ['#A9A9A9', '#FFA07A', '#B0E0E6', '#FFE4C4', '#BDB76B']
plt.pie(z, colors=color_theme)
plt.show()


# ### Customizing line styles

# In[31]:


x1 = range(0,10)
y1 = [10,9,8,7,6,5,4,3,2,1]

plt.plot(x, y)
plt.plot(x1, y1)


# In[41]:


plt.plot(x, y, ds='steps',lw=4)
plt.plot(x1, y1, ls='--', lw=5)


# ### Setting plot markers

# In[48]:


plt.plot(x,y,marker='1', mew=17)
plt.plot(x1,y1,marker='+', mew=16)


# In[ ]:




