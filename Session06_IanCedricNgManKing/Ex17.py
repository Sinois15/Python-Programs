# -*- coding: utf-8 -*-
"""
Casugol Ex.17
@author: Ian Cedric Ng Man King
ID:0338914
"""

#Read txt file carried over from carinventory (ex12)
file = open ("CarRecord.txt", "r")   
print (file.read())

#import libraries
import pandas as pd
import matplotlib.pyplot as plt 

#Creating dataframe from CarInventory data
data = pd.read_csv("CarRecord.txt", sep=':')
print(data)
#Displaying dataframe
print(data.info())
#Display Shape of the dataframe
print(data.shape)
#Display all the columns in the dataframe
print(data.columns)
#Renaming the columns of the dataframe
data.rename(columns={"RecordName": "Car ID","name": "Name","kind":"Kind","color":"Color","price":"Value" }, inplace=True)
#Display of all the columns in the dataframe after renaming
print("Columns: ", data.columns)

#Appending the data 
app_data = data.append(data) 
print (app_data.shape)
print(app_data)

#Remove Duplicated values 
app_data = app_data.drop_duplicates() 
print(app_data.shape)
app_data = data
print(data)

#See if the data contains null values or not 
print(data.isnull())

#Description of the dataframe and categories 
print(data.describe())
print(data['Car ID'].describe())
print(data['Name'].describe())
print(data['Kind'].describe())
print(data['Color'].describe())
print(data['Value'].describe())

#Frequency of Cateogorical data
print (data['Car ID'].value_counts().head(100))
print (data['Name'].value_counts().head(100))
print (data['Kind'].value_counts().head(100))
print (data['Color'].value_counts().head(100))
print (data['Value'].value_counts().head(100))

#Correlation of the variables in the dataframe
print(data.corr())

#Column extraction for 'Value' Column
val_col = data[['Value']] 
print(val_col)
print(type(val_col))


#Plotting the data
plt.rcParams.update({'font.size': 18, 'figure.figsize': (12, 10)}) 

# Chart to see Cars in Inventory with Car type and Number of Cars in Inventory
data['Car ID'].value_counts().plot(kind='bar', title="Cars in Inventory")
plt.xlabel("Unique Car ID")
plt.ylabel("Stock")
plt.show()
#Bar graph to see The Type of Cars and The value
data.plot(kind='bar', x='Car ID', y='Value', title='Price of each car in inventory') 

result = "a" + "a"
print(result)


