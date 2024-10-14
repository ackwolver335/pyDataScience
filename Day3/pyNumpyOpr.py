# importing the required modules
import numpy as np

# creating a 1D Array using numpy
arr1 = np.array([12,34,56])
print(arr1[0])

# creating a 2D Array here
arr2 = np.array([[1,2],[3,4],[5,6]])
print(arr2)
print(arr2.shape)

print("Dimensions of this array : " + str(arr2.ndim))                   # array's dimension
print("ByteSize of array's element : " + str(arr2.itemsize))            # arrays' bytesize of each element
print("Data type of the array is : " + str(arr2.dtype))                 # array's data type or its elements data type

# intializing with different data type
arr3 = np.array([[12,23],[34,45]],dtype = np.float64)                   # we can also use the data types like complex numbers
print("Changed Data type of array : \n" + str(arr3))

print("Size of this new array : " + str(arr3.size))                     # array's size for size of total elements
print("Shape of the array : " + str(arr3.shape))                        # array's shape for getting the array's rows and columns

# array of zeroes
arr4 = np.zeros((3,4))                                                 # similar to this we can also use ones()
print("Zeroes Array : \n" + str(arr4))

# array range method for creating the same
arr5 = np.arange(1,5)                                                   # this works similar to range() method for creating array of specific range
print("Array with arange() method : " + str(arr5))

# array linspace() method
arr6 = np.linspace(1,6,20)                                              # generating 20 numbers in b/w 1-6
print("Array created using linspace() method : " + str(arr6))

# reshaping an array
arr2.reshape(2,3)
print("Array after reshaping : " + str(arr2))                           # array reshaping

# ravel() method : Used in order to flatten the array and will not provide to the original dimensions of the array
print("Array after using ravel() method : " + str(arr2.ravel()))

# getting the minimum element of the array : min()
print("Array's minimum element : " + str(arr2.min()))

# getting the maximum element of the array : max()
print("Array's maximum element : " + str(arr2.max()))

# getting the sum of all the elements of the array : sum()
print("Array's elements total sum : " + str(arr2.sum()))

# getting the sum according to the axis of the array : sum(axis=value) [value can be 0 or 1]
print("Array's elements total sum according to the axis : " + str(arr2.sum(axis=0)))

# getting the square root of each of the element of the array : np.sqrt()
print("Square Root of each element of the array : \n" + str(np.sqrt(arr2)))

# getting the standard deviation of the elements of the array : np.std()
print("Standard Deviation of the array is : " + str(np.std(arr2)))

"""
    Some Basic Mathematical Operations on Arrays using Numpy :
    
    1. Addition : This oepration in numpy array is very useful as we don't have to use much different things like in Python Lists.
    2. Multiplication : This is done in the similar way that we do with the addition of numpy array.
    3. Division : And this one also works simply with the help of division sign '/'
    4. Matrix Dot Product : This one is similar to the one, that we usually do with the Matrix in our Mathematices Subject.
"""

# using some sample arrays here
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[5,6],[7,8]])

print("Addition of array's elements : " + str(array1 + array2))
print("Multiplication of the array's element : " + str(array1 * array2))
print("Division of the array's element is : " + str(array1 / array2))

# Matrix Dot Product
print("Matrix Dot Product : " + str(array1.dot(array2)))