# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:56:48 2020

@author: Lenovo
"""


import pandas as pd

country_df_from_file = pd.read_csv(r'C:\Users\Lenovo\PythonDemos\country.csv')
print(country_df_from_file,"\n")

# accessing the column of dataframe
print(country_df_from_file['Capital'],"\n")

#accessing the head values of column in a dataframe 
print(country_df_from_file['Capital'].head(2),"\n")
# head() specifies how many rows of data we wish the head function to return

# Tali function
print(country_df_from_file['Capital'].tail(2),"\n")

# loc[] with index, slicing 
print(country_df_from_file.loc[2],"\n")

print(country_df_from_file.loc[2:4],"\n")
print(country_df_from_file.loc[2:,'Country'],"\n")
print(country_df_from_file.loc[[2,4],:],"\n")
#print(country_df_from_file.loc[[2,4],:'Capital'],"\n")

# iloc[] accepts only integer
print(country_df_from_file.iloc[2:4],"\n")
# start inclusive , end exclusive

# accessing column using numerical column values
print(country_df_from_file.iloc[2:4,1],"\n")

print(country_df_from_file.iloc[[1,3,4],:],"\n")

# applying conditions
print(country_df_from_file[country_df_from_file['Country']=='India'],"\n")
# we can use AND [(condition) && (condition)]and OR conditions also negation [~(condition)]

