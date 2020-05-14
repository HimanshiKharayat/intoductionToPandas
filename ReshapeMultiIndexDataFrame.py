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

 # assigning multi index
course_df_from_file = pd.read_csv(r'C:\Users\Lenovo\PythonDemos\Courses.csv', 
                                  index_col=['Region','Course'])
course_df_from_file = course_df_from_file.sort_index()
print(course_df_from_file,"\n")


print(course_df_from_file.index,"\n") # returns multiindex 
 
course_stack = course_df_from_file.stack() # stacks the data frame on the basis of multiindex
print(course_stack,"\n") 

course_unstack = course_stack.unstack() # unstacking the stack data frames
print(course_unstack,"\n")  
 

#course_df_from_file = course_df_from_file.loc[(course_df_from_file.index.get_level_values(~(('Region')=='USA')))]
#print(course_df_from_file,"\n") 

# melt() will produce  a dataframe with one row of each
#course_melt = course_df_from_file.melt( id_vars=['Region','Course'], value_vars=['Name','Mentor'])
#print(course_df_from_file,"\n")

