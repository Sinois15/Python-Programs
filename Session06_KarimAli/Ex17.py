# -*- coding: utf-8 -*-
"""
Casugol Ex.17
@author: Karim
ID:0340689
"""

#Read txt file carried over from carinventory (ex12)
text = open ("List_of_vehicles.txt", "r")  
print (text.read())

#import panda dataframe 
import re
import pandas as pd

df = pd.read_csv("List_of_vehicles.txt", sep=',')
print(df)
#Information of dataframe
print(df.info())
#Details of Shape of the dataframe
print(df.shape)
#Details of all the columns in the dataframe
print(df.columns)
#Renaming the columns of the dataframe
df.rename(columns={         'Entry No.': 'Car ID','Brand': 'Company','Price':'Value' }, inplace=True)
#Details of all the columns in the dataframe after editing the rows
print(df.columns)

#Appending the data 
app_df = df.append(df) 
print (app_df.shape)
print(app_df)

#Remove Duplicated values 
app_df = app_df.drop_duplicates() 
print(app_df.shape)
app_df = df
print(df)

#See if the data contains null values or not 
print(df.isnull())

#Description of the dataframe and categories 
print(df.describe())
print(df['Company'].describe())
print(df['Type'].describe())
print(df['Color'].describe())

#Frequency of Cateogorical data
print (df['Company'].value_counts().head(100))
print (df['Type'].value_counts().head(100))
print (df['Color'].value_counts().head(100))

#Correlation of the variables in the dataframe
print(df.corr())

#Column extraction for 'PRICE' Column
price_col = df[['Value']] 
print(price_col)
print(type(price_col))


#Plotting the data
import numpy as np
import matplotlib.pyplot as plt 
plt.rcParams.update({'font.size': 18, 'figure.figsize': (12, 10)}) 

# Chart to see Cars in Inventory with Car type and Number of Cars in Inventory
df['Type'].value_counts().plot(kind='bar', title="Cars in Inventory")
plt.xlabel("Type of Car")
plt.ylabel("Number of Cars in Inventory")
plt.show()
#Bar graph to see The Type of Cars and The value
df.plot(kind='bar', x='Type', y='Value', title='Price of Car according to Types') 



