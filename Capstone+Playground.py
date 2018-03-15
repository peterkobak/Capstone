
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats


# In[2]:


data = pd.read_csv('C:\\Users\\rtenley\\Desktop\\complete.csv')


# In[3]:


data.head()


# In[4]:


data.firestation.value_counts()


# In[5]:


commercial = pd.read_csv('C:\\Users\\rtenley\\Desktop\\roland_fire_join.csv')


# In[6]:


commercial.head()


# In[7]:


commercial.firestation.value_counts()


# In[8]:


commercial.last_name.value_counts()


# In[9]:


gpsd = commercial.loc[commercial.last_name.isin(['GREATER PEORIA SANITARY & SEWAGE DISPOSAL DISTRICT']), :]


# In[10]:


gpsd.full_address.value_counts()


# In[11]:


adm = commercial.loc[commercial.last_name.isin(['ARCHER-DANIELS-MIDLAND COMPANY']), :]


# In[12]:


gpsd


# In[13]:


adm.PIN.value_counts()


# In[51]:


ovap = pd.read_csv('C:\\Users\\rtenley\\Desktop\\ovap.csv')


# In[52]:


ovap.Address.value_counts()


# In[53]:


ovap.head()


# In[54]:


mall1 = ovap.loc[ovap.Address.isin(['2200 W War Memorial DR']), :]


# In[18]:


ovap.drop(['Unnamed: 2', 'Unnamed: 3', 'NFF GPM', 'Flow Available'], axis = 1, inplace = True)


# In[55]:


mall1.columns


# In[20]:


mall1['OVAP Score'].value_counts()


# In[56]:


mall1['OVAP Score'].describe()


# In[57]:


ovap.loc[ovap.Address.isin(['5201 W War Memorial DR']), :]


# In[58]:


expo = ovap.loc[ovap.Address.isin(['1601 W Northmoor RD']), :]


# In[59]:


expo['OVAP Score'].value_counts()


# In[60]:


comm = pd.read_csv('C:\\Users\\rtenley\\Desktop\\commercial_property_list.csv')


# In[61]:


comm.head()


# In[27]:


comm.full_address.value_counts()


# In[62]:


comm


# In[29]:


ovap


# In[63]:


comm.rename(columns={'full_address': 'Address'}, inplace = True)


# In[64]:


comm.head()


# In[65]:


df = pd.concat([comm, ovap], ignore_index=True)


# In[68]:


df


# In[76]:


df.loc(columns = ['OVAP Score': 'OVAP'], inplace = True)

