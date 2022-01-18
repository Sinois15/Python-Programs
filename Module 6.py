#module 6

#Intro to pandas

#Creating DataFrame using DataFrame () method
import pandas as pd
data = {
 'cookies': [4, 5, 6, 7], 
 'cakes': [1, 2, 3, 4]
}
food = pd.DataFrame(data)
print (food, "\n")

#Creating Index
import pandas as pd
data = {
 'cookies': [4, 5, 6, 7], 
 'cakes': [1, 2, 3, 4]
}

#DataFrame formats the data as a table and if the indexes are not specified, it is numbered by default
food = pd.DataFrame(data, index=['Micheal', 'Tim', 'Mary', 'Lopez'])
print (food, "\n")

#Locating a customer name by using loc [] method
print(food.loc['Tim'], "\n")

#Using Pandas to Read / Writing Data
#Reading and loading data into a DataFrame is simple. All you need is just a single line of code. 

#Reading Data from CSVs
import pandas as pd
df = pd.read_csv('purchases.csv')
print(df, "\n")

#Setting indexes in DataFrame by using index_col parameter
import pandas as pd
df = pd.read_csv('purchases.csv', index_col=0)
print(df, "\n")

#Reading Data from JSON file
import pandas as pd
#df = pd.read_json('purchases.json')
#print(df, "\n")

#Reading Data from SQL Database
import pandas as pd
import sqlite3
#con = sqlite3.connect("database.db")
#df = pd.read_sql_query("SELECT * FROM purchases", con)
#print(df, "\n")

#Examples on Writing Data as CSV, JSON, or SQL
#df.to_csv('new_purchases.csv')
#df.to_json('new_purchases.json')
#df.to_sql('new_purchases', con)

#Pandas DataFrame Operations
#There are many methods and operations that you can use for any analysis in DataFrame. In this topic, we will 
#cover the fundamental operations are commonly used.

#Printing out the first few roles for visual reference
import pandas as pd
movies_df = pd.read_csv ("IMDB-Movie-Data.csv", index_col="Title")
print (movies_df.head ())
#By default, the first 5 rows of the DataFrame will be printed when you are using the .head() method.
#Printing out the first 10 rows
print (movies_df.head (10))

#Printing out the last few rows for visual reference
print (movies_df.tail(2))

#Learning more about the data by using: .info() 
print (movies_df.info())

#Displaying the dimension of the table
print (movies_df.shape)
 
#Checking for duplicates
#Creating a sample duplicate by using the append () method
temp_df = movies_df.append(movies_df)
print (temp_df.shape)
#Removing duplicates
temp_df = temp_df.drop_duplicates()
print(temp_df.shape)

#keep argument and its common options: -
#first: Default option when left empty. Drop duplicates except for the first occurrence
#last: Drop duplicates except for the last occurrence
#false: Drop all duplicates 
temp_df = movies_df.append(movies_df) 
temp_df.drop_duplicates(inplace=True, keep=False)
print(temp_df.shape)

#Cleaning Up Column
#Displaying column name
print (movies_df.columns)

#Renaming Columns
#movies_df.rename(columns={
 #'Runtime (Minutes)': 'Runtime', 
 #'Revenue (Millions)': 'Revenue_millions'
 #}, inplace=True)
#print ("columns:\n", movies_df.columns)

#You can also create a list of names(in lowercase) to the column:-
#movies_df.columns = [col.lower() for col in movies_df]
#print ( movies_df.columns)

#Dealing with Missing Values or Null Values in Data
#Checking the cell’s null status using isnull() method
print (movies_df.isnull())
#Calculating number of nulls in each column
print (movies_df.isnull().sum())
#Removing Rows with null Value
print (movies_df.dropna())
#Removing Columns with null Value
print (movies_df.dropna(axis=1))

#Imputation: inserting values into null
#Extract column with null and create its own variable
revenue = movies_df['Revenue (Millions)']
#Fill the nulls using fillna() method
revenue_mean = revenue.mean()
revenue.fillna(revenue_mean, inplace=True)
print("sum:\n", movies_df.isnull().sum())

#Summary Information on Data by using the describe () method
print (movies_df.describe())

#Categorical description
print (movies_df['Genre'].describe())
#Calculating the frequency of all values in a column
print (movies_df['Genre'].value_counts().head(10))

#Generating the Relationship Between Variables using .corr() method
print (movies_df.corr())

#Slicing, Selection and Extraction in DataFrame
#Extracting of Data by Column
#When a column is being extracted, it returns a Series. To create a DataFrame, a list of column names 
#is required to be passed.
genre_col = movies_df[['Genre']]
print (type(genre_col))

#Adding another column name
subset = movies_df [['Genre', 'Rating']]
print(subset.head())
#Extracting of Data by Row
#Extracting Row based on the value in the indexed column by using .loc method
prom = movies_df.loc["Prometheus"]
print (prom)
#Extracting Row based on numerical indexed location by using .iloc method
prom = movies_df.loc["Prometheus"]
print (prom)

#Extracting Row within a selected range is similar to [start:stop:step]
#using .loc method
movie_subset = movies_df.loc['Prometheus':'Sing']
print(movie_subset)
#using .iloc method
movie_subset = movies_df.iloc[1:4]
print (movie_subset)


