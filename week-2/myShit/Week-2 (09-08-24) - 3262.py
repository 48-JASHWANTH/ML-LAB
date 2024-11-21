#!/usr/bin/env python
# coding: utf-8

# # Exp no - 2

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv(r'C:\Users\java\Downloads\gapminder-FiveYearData (1).csv')


# In[4]:


df


# In[5]:


df.head()


# In[6]:


df.head(10)


# In[7]:


df.shape


# In[8]:


df.columns


# In[9]:


df.dtypes


# In[10]:


df.info()


# In[11]:


country_df = df['country']


# In[12]:


country_df


# In[13]:


country_df.head()


# In[20]:


country_df.tail()


# In[14]:


country_df.tail(10)


# In[15]:


subset = df[['country','continent','year']]


# In[16]:


subset.head()


# In[17]:


subset.tail()


# In[18]:


df.loc[0]


# In[19]:


df['pop'] = df['pop'].astype('float64')


# In[20]:


df.dtypes


# In[21]:


df.tail(n=1)


# In[22]:


df.loc[[0,99,999]]


# In[23]:


df.iloc[1]


# In[24]:


df.iloc[99]


# In[25]:


df.iloc[-1]


# In[26]:


df.iloc[[0,99,999]]


# In[30]:


df.loc[:,['year','pop']].head()


# In[29]:


df.iloc[:,[2,4,-1]].head()


# In[32]:


small_range = list(range(5))
small_range


# In[35]:


subset = df.iloc[:,small_range]
subset


# In[36]:


df.loc[42,'country']


# In[37]:


df.iloc[42,0]


# In[40]:


df.iloc[[0,99,999],[0,3,5]]


# In[41]:


df.loc[[0,9,99],['country','lifeExp','gdpPercap']]


# In[42]:


df.loc[10:13,['country','lifeExp','gdpPercap']]


# In[44]:


df.head(n=10)


# In[45]:


df.groupby('year')['lifeExp'].mean()


# In[49]:


mg = df.    groupby(['year','continent'])    [['lifeExp','gdpPercap']].    mean()
mg


# In[50]:


mg.reset_index().head(15)


# In[51]:


df.groupby('continent')['country'].nunique()


# # Exp no - 3

# In[52]:


df1 = pd.read_csv(r'C:\Users\java\Downloads\iris (1).csv')
df1


# In[53]:


type(df1)


# In[54]:


df1.shape


# In[55]:


df1.columns


# In[56]:


df1['species'].unique()


# In[57]:


df1['species'].nunique()


# In[58]:


d = {'Iris-satosa':0,
    'Iris-versicolor':1,
    'Iris-verginica':2}

df1['species'] = df1['species'].map(d)
df1.head()


# In[59]:


df.tail()


# In[63]:


import numpy as np
np.unique(df1['species'])


# In[74]:


df2 = pd.read_csv(r'C:\Users\java\Desktop\hi.txt',header = None)
df2


# In[ ]:




