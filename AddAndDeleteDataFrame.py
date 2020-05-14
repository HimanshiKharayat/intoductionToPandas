# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:14:37 2020

@author: Lenovo
"""



import pandas as pd

country_df_from_file = pd.read_csv(r'C:\Users\Lenovo\PythonDemos\country.csv')
print(country_df_from_file,"\n")

# adding a column to the data frame
#set a column's cells to a single value
country_df_from_file['Population'] = 13000000  
print(country_df_from_file,"\n")

# assigning different values to the column
country_df_from_file['Population'] = [13000000,1002000,3323444,2334555,5545544] 
#since column already exists , it will override the values to the cells of the column 
print(country_df_from_file,"\n")

#deleting a column in a data frame
del country_df_from_file['Population']
print(country_df_from_file,"\n")
 
country_df_from_file.loc[-1] = ['Afghanistan','Kabul']
#if index -1 already present it will simply override it else will be created
print(country_df_from_file,"\n")

#modifying index of data frame
country_df_from_file.index = country_df_from_file.index + 1
#increments the value of each row index by one
print(country_df_from_file,"\n")

# sorting the index values
country_df_from_file = country_df_from_file.sort_index()
print(country_df_from_file,"\n")

# Dropping the rows by index value
country_df_from_file = country_df_from_file.drop(country_df_from_file.index[5])
print(country_df_from_file,"\n")

# Seting customize index 
index_values =  [13000000,1002000,3323444,2334555,5545544]
country_df_from_file.index = index_values
print(country_df_from_file,"\n")

# to Reset the index values 
country_df_from_file = country_df_from_file.reset_index()
# it adds a new column containing the old index with header 'index' 
print(country_df_from_file,"\n")

# deleting  a column by using drop() rather than del command
country_df_from_file = country_df_from_file.drop(columns=['index'])
print(country_df_from_file,"\n")



