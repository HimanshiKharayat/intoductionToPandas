# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:45:12 2020

@author: Lenovo
"""


import pandas as pd

coun_list = ['India','USA','France','Japan','Russia']
cap_list = ['Delhi','Washington','Paris','Tokyo','Mossco']
coun_tuple = list(zip(coun_list, cap_list))
tup_df = pd.DataFrame(coun_tuple, columns = ['Country','Capital']) #Creating data frame
print(tup_df,"\n")

#Exporting rhe data frame to country.csv file 
tup_df.to_csv(r'C:\Users\Lenovo\PythonDemos\country.csv', index = False) #once this line is executed .csv file is created

#recovering the data which we have exported to csv file
country_df_from_file = pd.read_csv(r'C:\Users\Lenovo\PythonDemos\country.csv')
print(country_df_from_file)

#avacado_data = pd.read_csv('https://www.kaggle.com/neuromusic/avocado-prices')