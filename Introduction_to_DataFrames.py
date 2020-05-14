# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:49:14 2020

@author: Lenovo
"""


import pandas as pd

empty_dataFrame = pd.DataFrame()
print("empty data frame")
print(empty_dataFrame,"\n")

coun_list = ['India','USA','France','Japan','Russia']
cap_list = ['Delhi','Washington','Paris','Tokyo','Mossco']

#creating data frame using lists
coun_df = pd.DataFrame(coun_list)
print("Data frame using lists")
print(coun_df,"\n")

df = pd.DataFrame(index = coun_list,data = cap_list)
print("Data frame using two lists")
print(df,"\n")

print(df.values,"\n")
print(df.index)
#coun = ['India','USA','France','Japan','Russia']
#cap = ['Delhi','Washington','Paris','Tokyo','Mossco']


