# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:17:24 2020

@author: Lenovo
"""


import pandas as pd
import glob 
import os

path = r'C:\Users\Lenovo\PythonDemos'
filenames = glob.glob(path + "/*.xlsx")

concat_all_files = pd.DataFrame()
skip_rows = [0]
#required_rows = [0]
#df = pd.read_excel(file, sheet_name=None, skiprows=None, nrows=None, usecols=required_cols, header=None, index_col=None)

for file in filenames:
     
    df = pd.read_excel(file, sheet_name=None, skiprows=skip_rows, nrows=None, usecols=None,userows=None , header=None, index_col=None)
    
    concat_all_single_file = pd.concat(df,sort=False)
    
    concat_all_single_file['filename'] = os.path.basename(file)
    
    concat_all_files = concat_all_files.append(concat_all_single_file)
    
print(df)
writer = pd.ExcelWriter(r'C:\Users\Lenovo\PythonDemos\combine.xlsx')

concat_all_files.to_excel(writer)

writer.save()
