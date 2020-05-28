# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:20:05 2020

@author: Lenovo
"""


import pandas as pd
import glob 
import os

#pd.read_csv(filepath_or_buffer = "C:\Users\Lenovo\PythonDemos\data1.csv")
#pd.read_csv("C:\Users\Lenovo\PythonDemos\data1.csv", header = [1,2])

path = r'C:\Users\Lenovo\PythonDemos'
filenames = glob.glob(path + "/*.csv")

for file in filenames:
    df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('', "*.csv"))))


