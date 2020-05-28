# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:59:07 2020

@author: Lenovo
"""



import numpy as np


array_one = np.array([0,1,2,4,6,7,3,9])
print(array_one)
num = [11,22,33,44,55,66,77,88]
array_two = np.array(num)
print(array_two)

# arrayof zeroes
array_of_zeroes = np.zeros((2,3))
print("\n",array_of_zeroes)

#array of ones
array_of_ones = np.ones((3,2))
print("\n",array_of_ones)

# converting ones array into integer
array_of_ones = np.ones((3,2), dtype = np.int32)
print("\n",array_of_ones)

array_of_empty = np.empty((3,2))
#here  the output consists of ones because it is already allocated in the memory
print("\n",array_of_empty)

array_of_eye = np.eye(4)
# digonal element contains one rest zero
print("\n",array_of_eye)

# np.arange() 
array_of_even = np.arange(2,24,2)
print("\n",array_of_even)

array_of_floats = np.arange(1,3,0.3)
print("\n",array_of_floats)

# 2D arrays
array_2D = np.array([(1,2,3,4,5),(6,7,8,9,0)])
print("\n 2Darray",array_2D)
print("\n", array_2D.shape)  #gives size of array

print("\n",np.arange(8)) # lb=0, ub=8,interval=1

# reshaping the array created by arange()
array_nd = np.arange(8).reshape(2,4) #must have the correct no. of elements to reshape
print("\n",array_nd)

array_ones = np.ones_like(array_nd)
#similar to np.ones() but here the shape is of array_nd
print("\n",array_ones)

#3D array
x=np.arange(36).reshape(3,4,3) 
print("\n",x)

