# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:23:24 2020

@author: Lenovo
"""

import pandas as pd

coun_list = ['India','USA','France','Japan','Russia']
cap_list = ['Delhi','Washington','Paris','Tokyo','Mossco']

#creating data frame using Tuples
coun_tuple = list(zip(coun_list, cap_list))
print(coun_tuple,"\n")
tup_df = pd.DataFrame(coun_tuple)
print("Data frame using tuples")
print(tup_df,"\n")

print("Data frame using tuples and assigning the column/header name")
tup_df = pd.DataFrame(coun_tuple, columns = ['Country','Capital'])
print(tup_df,"\n")

#new dataFrame using pandas Series object
coun_dict = {'Country name':pd.Series(coun_list),'Capital' : pd.Series(cap_list)}
dict_df = pd.DataFrame(coun_dict)
print("Data frame using Dictionary")
print(dict_df,"\n")