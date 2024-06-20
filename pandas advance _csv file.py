#!/usr/bin/env python
# coding: utf-8

# In[5]:


print("osama")


# In[6]:


import pandas as pd


# In[11]:


df = pd.read_csv('customers-100.csv')


# In[12]:


df


# In[13]:


df = pd.read_csv('customers-100.csv',header = None)
df


# In[17]:


df = pd.read_csv('customers-100.csv', skiprows = 2)
df


# In[32]:


df = pd.read_csv('customers-100.csv',  usecols = ['Customer Id	','First Name	','Last Name	'])
df


# In[33]:


df = pd.read_csv('customers-100.csv')
df


# In[34]:


#series and data frame..
type(df)


# In[35]:


df


# In[36]:


#one col acces.
df.Company	


# In[39]:


df['Company']


# In[40]:


df


# In[41]:


type(df['Company'])


# In[42]:


l = [1,2,3,4,5]
s = pd.Series(l)
print(s)


# In[43]:


type(s)


# In[44]:


s[1]


# In[45]:


s[2:]


# In[46]:


d = pd.Series([100,200,300],index = ["osama","bin","laden"])
d


# In[47]:


type(d)


# In[48]:


#acces.
d["osama"]


# In[49]:


#index..
d.index


# In[51]:


d["osama":"bin"]


# In[52]:


d


# In[53]:


#change index..
d.reset_index(drop=True)


# In[54]:


d.reset_index()


# In[55]:


pd.DataFrame(d)


# In[56]:


df


# In[58]:


df.shape


# In[59]:


df.columns


# In[61]:


list(df.columns)


# In[63]:


df.head(5) #first five row


# In[64]:


df.head(3)


# In[65]:


df.tail(7)


# In[66]:


df.sample(5)


# In[69]:


df.info()


# In[71]:


import pandas as pd
df.dtypes


# In[73]:


#one col acces.
df['Company']


# In[74]:


type(df['Company'])


# In[78]:


#series  to dataframe..
s = pd.Series([2,3,4,5], index = [100,"osama","bin",2])
s


# In[80]:


d = pd.DataFrame(s)
d


# In[81]:


#col created..
d['new_column'] = "osama"
d


# In[87]:


d.column = ['id','name','new_name']
d


# In[88]:


d.reset_index()


# In[89]:


d.reset_index(drop = True)


# In[93]:


df.columns


# In[94]:


df.Company


# In[96]:


df.index


# In[97]:


df.columns


# In[99]:


df_subset = df[['Index','Company','Country']]
df_subset


# In[104]:


df3 = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")
df3


# In[105]:


df3.columns


# In[106]:


df3.info


# In[107]:


df3['Sex']


# In[108]:


df3.columns


# In[109]:


df3[['PassengerId','Fare','Pclass']]


# # #html
# 
# 

# In[113]:


pip install Lxml


# In[114]:


import lxml


# In[116]:


import pandas as pd
url_df = pd.read_html("https://www.basketball-reference.com/leagues/NBA_2021_per_game.html")


# In[117]:


url_df


# In[118]:


type(url_df)


# In[119]:


url_df[0]


# In[120]:


df4 = url_df
df4


# In[124]:


df4


# In[125]:


df4.shape


# In[126]:


df.columns


# In[127]:


df4.info()


# In[128]:


df4


# In[129]:


df4.to_csv("players.csv", index = False)


# # jsonn

# In[130]:


url = "https://opensource.adobe.com/Spry/samples/data_region/JSONDataSetSample.html"
pd.read_json(url)


# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




