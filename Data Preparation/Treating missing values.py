#!/usr/bin/env python
# coding: utf-8

# # Data Preparation Basics
# ## Segment 2 - Treating missing values

# In[3]:


import numpy as np
import pandas as pd 

from pandas import Series, DataFrame


# ### Figuring out what data is missing

# In[4]:


missing = np.nan
series_obj = Series(['row 1','row 2',missing,'row 4','row 5',missing,'row 7','row 8',missing,'row 10'])
series_obj


# In[5]:


series_obj.isnull()


# ### Filling in for missing values

# In[12]:


np.random.seed(25)
DF_obj = DataFrame(np.random.rand(49).reshape(7,7))
DF_obj


# In[13]:


DF_obj.loc[1:4, 1]=missing
DF_obj.loc[3:6, 5]=missing
DF_obj


# In[14]:


filled_DF = DF_obj.fillna(0)
filled_DF


# In[16]:


filled_DF = DF_obj.fillna({0:0.1,1:0.2,5:1.33})
filled_DF


# In[17]:


fill = DF_obj.fillna(method='ffill')
fill


# ### Counting missing values

# In[28]:


np.random.seed(25)
DF_obj = DataFrame(np.random.rand(49).reshape(7,7))
DF_obj.loc[3:5, 0]=missing
DF_obj.loc[1, 0]=missing
DF_obj.loc[1:6, 6]=missing
DF_obj.loc[4, 4]=missing
DF_obj


# In[29]:


DF_obj.isnull().sum()


# In[31]:


DF_obj.isnull().sum(axis=1)


# ### Filtering out missing values

# In[32]:


DF_no_NaN = DF_obj.dropna()
DF_no_NaN


# In[33]:


DF_no_NaN = DF_obj.dropna(axis=1)
DF_no_NaN

