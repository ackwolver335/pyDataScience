"""
    Getting started with other Operations of Numpy Array :

    1. Slicing : This is the simplest method that is been done with the help of ':' in Python Lists and thus so it supports the negative indexing also.
    And in case we try the same thing with the Numpy Array then it will work smoothly in that particular case also. Here also the negative indexing is 
    been supported in order to gather some data from the array.

    2. Iterating : As we all know that the 'for' loop is been used in order to make the lists iterable in the similar way here also we uses the for 
    loop in order to iterate over to the Numpy Arrays.
"""

# importing the required modules
import numpy as np

# creating a list here
l1 = [1,2,3,4,5,6,7]
print("Slicing a particular part of the list : " + str(l1[1:4]))                    # slicing in lists

# creating a numpy array
a1 = np.array([1,2,3,4,5,6])
print("Making a partition from the Numpy Array : " + str(a1[1:4]))

# creating a multidimensional array
array1 = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

# let us check the difference of the slicing in case of multidimensional array
print("Getting a particular element using slicing in multidimensional array : " + str(array1[1,3]))                 # 2st dimension 4rth element

# Getting the all data of the 2nd column of the array
print("Data of the 2nd column of the array : " + str(array1[0:,2]))                                                 # 2nd Column of the array

# another way of accessing elements
print("Getting specific elements of the array : " + str(array1[2,0:3]))                                             # last row 3 elements

# printing the rows of the Numpy array using for loop
for rows in array1:
    print(rows)

# flattening the array in a single line format and printing using flat keyword
for cells in array1.flat:
    print(cells,end = " ")

print()

# Sticking two array's together in Numpy
# creating two more different arrays for sticking purpose
arr1 = np.arange(6).reshape(3,2)
arr2 = np.arange(6,12).reshape(3,2)

print("Vertical Stacking : \n" + str(np.vstack((arr1,arr2))))                           # vertical sticking/stacking

# let us try the same thing with Horizontal Stacking/Sticking
print("Horizontal Stacking : \n" + str(np.hstack((arr1,arr2))))

# splitting the array in more different format
arr3 = np.arange(30).reshape(2,15)
print("Array Splitted in 3 different arrays : \n" + str(np.hsplit(arr3,3)))

# splitted array
splitted_array = np.hsplit(arr3,3)
print("Array's First Element after splitting : \n" + str(splitted_array[0]) + "\nArray's Second Element after splitting : \n" + str(splitted_array[1]))

# Note : Similarly we can do the vertical split with the vsplit() method
# Let's get started with the Boolean Array
arr4 = arr3 > 5
print("Boolean array formed here is : \n" + str(arr4))

# Setting all the values as -1 which are true in arr3
arr3[arr4] = -1
print("Array after changing all the values which were true with -1 : \n" + str(arr3))