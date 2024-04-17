#npref.py

'''
This python file is meant to contain the basics of numpy, as a reference for numpy users. 

Source: https://numpy.org/doc/stable/user/quickstart.html#the-basics

Author: Pachie Ackerman
'''

import numpy as np


#dimentions are called axes
arr = np.array([1, 2, 3])
arr.ndim # num of dims or axes
arr.shape # For a matrix with n rows and m columns, shape will be (n,m)
arr.size # total num of elements
arr.dtype #datatype of arr's elements. Element datatype can be passed to most array creation functions


#array creation
arr = np.array([1, 2, 3]) #convert from python list, NOT np.array(1, 2, 3)
arr = np.array([[1, 2, 3], [4, 5, 6]]) # 2 axes

#creating with placeholder content
np.zeros((2, 3, 4))
np.ones((1, 2))

#sequences
np.arange(5, 7, -2) #np version of python range, but returns a ndarray
np.linspace(1, 5, 5) # (start, end, totalnum), instead of (start, end, step)
#linspace end is inclusive where arange end is exclusive


#to force print the whole array, use:
import sys
np.set_printoptions(threshold=sys.maxsize)


#operations happen elementwise
# A * B is elementwise, for matrix mult use A @ B or A.dot(B)
# += and similar also work elementwise


#indexing, slicing, iterating
arr[4] #for 1D, same as python lists
arr[2, 3] #for larger dims, indexing is arr[row, col, etc...]

arr[3:5] #again, 1D same as python lists
arr[2:6, 7:8] #higher dims can have a slice in each dim
arr[:, 5] #like python, leaving things blank means include everything

for row in arr: #in higher dims, for looping will give the rows
    print(row)

for element in arr.flat: #or, use .flat to iter through everything
    print(element)

