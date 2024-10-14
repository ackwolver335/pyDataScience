"""
    Getting started with numpy Module
    Syntax for importing Numpy Module : import numpy

    1. creating an array with the help of numpy
    Ex : numpy.array([1,2,4])

    Benefits of using array on the place of Python Lists :
    1. Takes or Consumes less memory space.
    2. Faster as and when compared to the lists.
    3. Convinient to use with the help of the lists.

    Note : We can also perform other difference operations other the those that are performed over to the lines from 61-64
"""

# importing the required module
import numpy as np

# modules for checking the difference b/w the list and the array of numpy
import time
import sys

# creating a list here
list1 = range(1000)
print("Size of the list created here : " + str(sys.getsizeof(1) * len(list1)))

# creating an array with the same number of elements
array1 = np.arange(1000)
print("Size of the array : " + str(array1.size))

arr1 = np.array([1,2,3])                    # array created with the help of array
print("Accessing the array's element : " + str(arr1[0]))

# checking how the numpy array is convinient as compared to Python Lists
# creating similar size container first
size1 = 1000000

# some lists here
l1 = range(size1)
l2 = range(size1)

# some arrays here
ar1 = np.arange(size1)
ar2 = np.arange(size1)

# starting the timer for the creation of a list
start = time.time()
result = [(i + j) for i,j in zip(l1,l2)]
print("Time taken by Python Lists : " + str((time.time() - start) * 1000))

# another timer for checking the time of the array
start = time.time()
result = ar1 + ar2
print("Python Numpy Array took : " + str((time.time() - start) * 1000))

# Different Methods that we can perform over to the numpy array
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

# Operations
print("Numpy Array Addition : " + str(a1 + a2))
print("Numpy Array Subtraction : " + str(a1 - a2))
print("Numpy Array Multiplication : " + str(a1 * a2))
print("Numpy Array Division : " + str(a1 / a2))