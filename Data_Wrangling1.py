#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[4]:


df=pd.read_csv("Automobile_data.csv")


# In[5]:


print(df)


# In[6]:


df.shape


# In[7]:


df.index


# In[8]:


df.values


# In[9]:


df.columns


# In[12]:


df.replace("?",np.nan,inplace=True)


# In[14]:


df.head(10)


# In[15]:


df.tail(10)


# In[16]:


missing_data=df.isnull()


# In[17]:


missing_data.head(10)


# In[20]:


df.isnull().sum()


# In[23]:


df.isnull()


# In[26]:


for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


# In[27]:


df.describe()


# In[39]:


avg_norm=df["normalized-losses"].astype("float").mean()


# In[40]:


print("Average of normalized losses:",avg_norm)


# In[31]:


avg_stroke=df["stroke"].astype("float").mean(axis=0)


# In[32]:


print("Average of Stroke:",avg_stroke)


# In[33]:


avg_bore=df["bore"].astype("float").mean(axis=0)


# In[34]:


print("Average of Bore:",avg_bore)


# In[35]:


avg_horsepower=df["horsepower"].astype("float").mean(axis=0)


# In[36]:


print("Average of Horsepower:",avg_horsepower)


# In[37]:


avg_peakrpm=df["peak-rpm"].astype("float").mean(axis=0)


# In[38]:


print("Average of peak-rpm:",avg_peakrpm)


# In[41]:


df["normalized-losses"].replace(np.nan,avg_norm,inplace=True)


# In[42]:


df.head(10)


# In[44]:


df["stroke"].replace(np.nan,avg_stroke,inplace=True)


# In[45]:


df["bore"].replace(np.nan,avg_bore,inplace=True)


# In[46]:


df["horsepower"].replace(np.nan,avg_horsepower,inplace=True)


# In[47]:


df["peak-rpm"].replace(np.nan,avg_peakrpm,inplace=True)


# In[48]:


df.head(10)


# In[50]:


print(df)


# In[52]:


df['num-of-doors'].value_counts()


# In[53]:


df['num-of-doors'].replace(np.nan,"four",inplace=True)


# In[54]:


print(df)


# In[55]:


df.dropna(subset=["price"],axis=0,inplace=True)


# In[56]:


df.reset_index(drop=True,inplace=True)


# In[57]:


print(df)


# In[59]:


df.dtypes


# In[60]:


df[["bore","stroke","price","peak-rpm"]]=df[["bore","stroke","price","peak-rpm"]].astype("float")


# In[61]:


df.dtypes


# In[62]:


df[["normalized-losses"]]=df[["normalized-losses"]].astype("int")


# In[63]:


df.dtypes


# In[65]:


df["city-L/100km"]=235/df["city-mpg"]


# In[66]:


df.head(10)


# In[70]:


df.drop(["newcol-L/100km"],axis=1)


# In[71]:


df["highway-L/100km"]=235/df["highway-mpg"]


# In[72]:


df.head(10)


# In[73]:


df.drop(["newcol-L/100km"],axis=1)


# In[74]:


df['length']=df['length']/df['length'].max()


# In[75]:


df['width']=df['width']/df['width'].max()


# In[77]:


df['height']=df['height']/df['height'].max()


# In[78]:


df.head(10)


# In[83]:


del df["newcol-L/100km"]


# In[84]:


df.head(10)


# In[85]:


print(df)


# In[87]:


df['height'].head(10)


# In[88]:


df['width'].head(10)


# In[89]:


df['length'].head(10)


# In[ ]:


df.to_csv('Pract_1')

