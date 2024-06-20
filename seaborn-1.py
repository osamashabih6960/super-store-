#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


sns.get_dataset_names()


# In[4]:


df = sns.load_dataset('tips')


# In[5]:


df


# In[6]:


#numerical data plot..
sns.relplot() # relation b/w two variables.


# In[7]:


sns.relplot(x = 'total_bill', y = 'tip', data = df)


# In[8]:


sns.scatterplot(x = df.total_bill, y = df.tip, data = df)


# In[9]:


#find smoker.
sns.scatterplot(x = df.total_bill, y = df.tip, data = df,hue = 'smoker')


# In[11]:


#bill increase also tips increase..
sns.relplot(x = 'total_bill', y = 'tip', data = df, hue = 'smoker')


# In[12]:


sns.relplot(x = 'total_bill', y = 'tip', data = df, hue = 'smoker')


# In[13]:


sns.relplot(x = 'total_bill', y = 'tip', data = df, hue = 'size')


# In[14]:


sns.relplot(x = 'total_bill', y = 'tip', data = df, style= 'smoker', hue = 'smoker')


# In[15]:


sns.relplot(x = 'total_bill', y = 'tip', data = df, style= 'smoker', hue = 'time')


# In[16]:


value = np.random.randn(100)


# In[17]:


value


# In[18]:


value = np.random.randn(100)
time = np.arange(100)


# In[19]:


time


# In[20]:


value


# In[25]:


value = np.random.randn(100).cumsum()
time = np.arange(100)
df = pd.DataFrame({'time':time, 'value':value})


# In[26]:


df


# In[27]:


#relplot..
sns.relplot(x = 'time', y = 'value', kind = 'line', data = df, sort = True)


# In[28]:


fmri = sns.load_dataset('tips')


# In[29]:


fmri


# In[32]:


sns.relplot(x = 'tip', y = 'sex', kind = 'line', data = fmri)


# In[ ]:





# In[33]:


fmri.info()


# In[34]:


sns.relplot(x = 'tip', y = 'sex', kind = 'line', data = fmri, ci = 'sd')


# In[35]:


sns.relplot(x = 'tip', y = 'sex', kind = 'line',estimator = None, data = fmri, ci = 'sd')


# In[37]:


sns.relplot(x = 'tip', y = 'sex', kind = 'line', data = fmri, ci = 'sd',hue = 'event')


# In[38]:


sns.relplot(x = 'tip', y = 'sex', kind = 'line', data = fmri, ci = 'sd', markers = True)


# In[43]:


df1 = sns.load_dataset('tips')


# In[44]:


df1


# In[46]:


sns.relplot(x = 'total_bill', y = 'tip', hue = 'smoker', data = df1, col = 'time')


# In[47]:


sns.relplot(x = 'total_bill', y = 'tip', hue = 'smoker', data = df1, col = 'time')


# In[48]:


sns.relplot(x = 'total_bill', y = 'tip', hue = 'smoker', data = df1, col = 'size')


# In[50]:


sns.scatterplot(x = 'total_bill', y = 'tip', data = tips)


# In[51]:


df1


# In[53]:


sns.catplot(x = 'day',y = 'total_bill', data = df1)


# In[54]:


sns.catplot(x = 'day',y = 'total_bill', data = df1, kind = 'swarm')


# In[56]:


sns.catplot(x = 'day',y = 'total_bill', data = df1, kind = 'box')


# In[58]:


sns.catplot(x = 'day',y = 'total_bill', data = df1, kind = 'violin')


# In[59]:


sns.catplot(x = 'day',y = 'total_bill', data = df1, kind = 'boxen')


# In[60]:


sns.barplot(x = 'day',y = 'total_bill', data = df1)


# In[66]:


sns.jointplot(x = tips.total_bill, y = tips.df1)


# In[73]:


tip = sns.load_dataset('tips')


# In[74]:


tip


# In[76]:


sns.jointplot(x = tips.total_bill,y = tips.tip)


# In[77]:


sns.jointplot(x = tips.total_bill,y = tips.tip, kind = 'reg')


# In[78]:


sns.jointplot(x = tips.total_bill,y = tips.tip, kind = 'hex')


# In[80]:


sns.jointplot(x = tips.total_bill,y = tips.tip, kind = 'kde')


# In[81]:


#pair plot..
tip


# In[82]:


sns.pairplot(tip)


# In[85]:


sns.pairplot(tips, hue = 'smoker')


# In[88]:


sns.pairplot(tips, hue = 'smoker', palette = 'coolwarm')


# In[89]:


#boxplot..
sns.boxplot(x = 'day', y = 'total_bill', data = tip)


# In[91]:


sns.boxplot(x = 'day', y = 'total_bill', data = tip, palette = 'rainbow')


# In[93]:


sns.boxplot(data = tip, palette = 'rainbow',orient = 'h')


# In[97]:


tip = tips[['total_bill','tip','size']]


# In[98]:


tip


# In[99]:


tip.corr()


# In[100]:


sns.heatmap(tip.corr(), cmap = 'coolwarm')


# In[102]:


df = sns.load_dataset("tips")


# In[103]:


df


# In[104]:


sns.countplot(x = "sex", data = df)


# In[106]:


sns.lmplot(x = 'total_bill', y = 'tip', data = df)


# In[107]:


sns.lmplot(x = 'total_bill', y = 'tip', data = df,height = 15)


# In[108]:


sns.lmplot(x = 'total_bill', y = 'tip', data = df,height = 15)


# In[109]:


sns.lmplot(x = 'total_bill', y = 'tip', data = df,height = 15, aspect = 1)


# # Bokeh

# In[110]:


pip install bokeh


# In[111]:


import bokeh.io
import bokeh.plotting
bokeh.io.output_notebook()


# In[112]:


from bokeh.sampledata.iris import flowers
from bokeh.plotting import figure, output_file, show


# In[114]:


flowers


# In[116]:


output_file('test.html')
p = figure(title = 'test_flower')
p.xaxis.axis_label = "petal_length"
p.yaxis.axis_label = "petal_width"
p.circle(flowers['petal_length'], flowers['petal_width'])
show(p)


# In[117]:


output_file('test.html')
p = figure(title = 'test_flower')
p.xaxis.axis_label = "petal_length"
p.yaxis.axis_label = "petal_width"
p.line(flowers['petal_length'], flowers['petal_width'])
show(p)


# In[118]:


x = [1,2,3,4]
y = [3,8,4,7]
output_file("line.html")
p = figure(title = "line chart")
p.line(x,y)
show(p)


# In[120]:


x = [1,2,3,4]
y = [3,8,4,7]
output_file("line.html")
p = figure(title = "line chart")
p.scatter(x,y)
show(p)


# In[122]:


x = [1,2,3,4]
y = [3,8,4,7]
output_file("line.html")
p = figure(title = "line chart")
p.scatter(x,y, size = 20, fill_color = 'red')
show(p)


# In[125]:


x = [1,2,3,4]
y = [3,8,4,7]
output_file("line.html")
p = figure(title = "line chart")
p.scatter(x,y, size = 20, fill_color = 'red', legend_label = "this is my data")
show(p)


# In[ ]:





# In[ ]:




