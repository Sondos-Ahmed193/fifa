#!/usr/bin/env python
# coding: utf-8

# In[1]:


#loading the requird libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


fifa = pd.read_csv('players_20.csv')


# In[3]:


fifa.head()


# In[4]:


for col in fifa.columns:
    print(col)


# In[5]:


fifa.shape


# In[6]:


fifa['nationality'].value_counts()


# In[7]:


fifa['nationality'].value_counts()[0:10]


# In[8]:


fifa['nationality'].value_counts()[0:5].keys()


# In[9]:


plt.figure(figsize=(8,5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color="g")
plt.show()


# In[10]:


player_salary = fifa[['short_name','wage_eur']]


# In[11]:


player_salary.head()


# In[12]:


player_salary = player_salary.sort_values(by=['wage_eur'],ascending=False)


# In[13]:


player_salary.head()


# In[14]:


plt.figure(figsize =(8,5))
plt.bar(list(player_salary['short_name'])[0:5],list(player_salary['wage_eur'][0:5]),color='y')
plt.show()


# In[15]:


fifa['nationality']=='Germany'


# In[16]:


#Germany
Germany = fifa[fifa['nationality']=='Germany']
Germany.head()


# In[17]:


Germany.sort_values(by=['height_cm'],ascending=False).head()


# In[18]:


Germany.sort_values(by=['weight_kg'],ascending=False).head()


# In[19]:


Germany.sort_values(by=['wage_eur'],ascending=False).head()


# In[25]:


Germany[['short_name','wage_eur']].sort_values(by=['wage_eur'],ascending=False).head()


# In[27]:


#shooting
player_shooting = fifa[['short_name','shooting']]
player_shooting.sort_values(by=['shooting'],ascending=False).head()


# In[29]:


#defending
player_defending = fifa[['short_name','defending','nationality','club']]
player_defending.head()


# In[30]:


player_defending.sort_values(by=['defending'],ascending=False).head()


# In[38]:


real_madrid=fifa[fifa['club']=='Real Madrid']
real_madrid.head()


# In[39]:


real_madrid.sort_values(by=['wage_eur'],ascending = False).head()


# In[40]:


real_madrid.sort_values(by=['shooting'],ascending =False).head()


# In[41]:


real_madrid.sort_values(by=['defending'],ascending =False).head()


# In[43]:


real_madrid['nationality'].value_counts()


# In[ ]:




