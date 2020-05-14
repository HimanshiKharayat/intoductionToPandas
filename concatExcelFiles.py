# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:14:17 2020

@author: Lenovo
"""


import pandas as pd
import glob

filenames = glob.glob("./" + "/*.xlsx")

excels = [pd.ExcelFile(name) for name in filenames]

frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

frames[1:] = [df[1:] for df in frames[1:]]

combined = pd.concat(frames)

combined.to_excel("c1.xlsx", header=False, index=False)