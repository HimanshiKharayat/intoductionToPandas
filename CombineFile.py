# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:49:38 2020

@author: Lenovo
"""

import pandas as pd

excel_names = ["classdata1.xlsx", "classdata2.xlsx", "classdata3.xlsx", "classdata4.xlsx"]

excels = [pd.ExcelFile(name) for name in excel_names]

frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

# delete the first row for all frames except the first
# i.e. remove the header row -- assumes it's the first
frames[1:] = [df[1:] for df in frames[1:]]

combined = pd.concat(frames)


combined.to_excel("c.xlsx", header=False, index=False)