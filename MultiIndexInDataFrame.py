# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:45:30 2020

@author: Lenovo
"""


# multi index for a row is composite key made up of more that one column
# each index is  known as level

import pandas as pd

course_df_from_file = pd.read_csv(r'C:\Users\Lenovo\PythonDemos\Courses.csv')
print(course_df_from_file,"\n")

print(course_df_from_file['Course'].unique(),"\n")