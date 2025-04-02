#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("Comcast_telecom_complaints_data.csv")
df

df.head()

df.tail()

df.sample(5)

df.shape            
df.shape           

df['Received Via'].unique()

a =df['City'].unique()
df['City'].unique()

df['Status'].unique()
df.isnull().sum()
df.info()
df['Status'].unique()
df['New_Status'] = ['Closed'    if i == 'Solved' or i == 'Closed'  else 'Open'       for i in  df['Status'] ]

df['New_Status'].unique()

df['Date_month_year'] = df['Date_month_year'].apply(pd.to_datetime)
df.info()


df['Zip code'] = df['Zip code'].astype(object)
#df.info()

df['Date_month_year'].value_counts()

df['Date_month_year'].value_counts().plot()
plt.xlabel('Date')
plt.ylabel('Complaint Frequency')
plt.title('Daily Complaint Plot')

plt.show()

df['State'].value_counts()[ : 10]


df['State'].value_counts()[ : 10].plot.bar(figsize = (10,10))
df.groupby(['State', 'New_Status']).size()

statewise_complaints = df.groupby(['State', 'New_Status']).size().unstack()
statewise_complaints

statewise_complaints.plot.bar(figsize = (10,10), stacked = True)

