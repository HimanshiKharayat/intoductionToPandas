# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:22:43 2020

@author: Lenovo
"""


import pandas as pd

df = pd.read_csv(r"C:\Users\Lenovo\PythonDemos\data1.csv")
df1 = pd.read_csv(r"C:\Users\Lenovo\PythonDemos\data2.csv")
df2 = df1.append(df)
df2 = pd.DataFrame(df2,columns= ['Name','Class'])
df2.to_csv(r"C:\Users\Lenovo\PythonDemos\dataFile.csv")
print(df2)