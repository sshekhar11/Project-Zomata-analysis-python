#!/usr/bin/env python
# coding: utf-8

# # Project ZOMATO
# 

# In[1]:


#Step 1 importing libraries
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# # Step 2 calling the dataset or creating dataframe.

# In[2]:


dataframe = pd.read_csv("Zomato data .csv")
print(dataframe)


# In[3]:


dataframe


# # converting the data type of column =rate

# In[4]:


def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)
dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# In[5]:


dataframe.info()


# # Types of restro

# In[6]:


dataframe.head()


# In[7]:


sns.countplot(x=dataframe['listed_in(type)'] )
plt.xlabel("Types of Resturant")


# In[8]:


#conclusion= majority of restorant are of dinning type.
# wherevrer 'types' is asked use bar charts.


# In[9]:


dataframe.head()


# In[10]:


grouped_d= dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_d})
plt.plot(result, c="orange", marker="o")
plt.xlabel("Types od restro", c="red", size=20)
plt.ylabel("Votes", c="brown", size=20)


# In[11]:


#conclusion = dinning has most number of votes.


# In[12]:


#finding the rating of restro. Histogram


# In[13]:


dataframe.head()


# In[14]:


plt.hist(dataframe['rate'],bins=10)
plt.title("rating distribution")
plt.show()


# In[15]:


#the majority of restro are getting rating betweeen 3.5 to 4.


# In[16]:


dataofcouple=dataframe['approx_cost(for two people)']
sns.countplot(x=dataofcouple)


# In[17]:


#by this graph we can conclude that average price of ordering is 300.


# In[18]:


plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y= 'rate', data= dataframe)   


# In[19]:


#we can conclude that online orders are more.


# In[20]:


dataframe.head(10)


# In[26]:


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="crest", fmt= 'd' )
plt.title("Heatmap")
plt.xlabel("online_order")
plt.ylabel("Listed_in(type)")
plt.show()


# # conclusion= dinning restro have more offline orders than online, whereas in other three types online orders are more than offline one.
# 

# In[ ]:




