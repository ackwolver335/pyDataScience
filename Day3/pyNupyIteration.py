"""
    Getting started with Numpy Array's Iterations :
"""

# numpy module
import numpy as np

a1 = np.arange(12).reshape(3,4)                     # array for iteration

print("Flattening the array using 2 for loops : ")
for row in a1:
    for cell in row:
        print(cell,end = " ")
print()

# another best alternative for flattening the elements of the array
print("Flattening the array using flatten() method : ")
for row in a1.flatten():
    print(row,end = " ")
print()

# Another way to do it with the help of nditer() of Numpy
print("Doing the same thing with nditer() method : ")
for row in np.nditer(a1,order = 'C'):
    print(row,end = ' ')
print()

# Fortan Order
print("Fortan Order (Column-Wise Order) : ")
for row in np.nditer(a1,order = 'F',flags=['external_loop']):
    print(row)

# Changing the value of the array at the runtime inside the loop
for row in np.nditer(a1,order = 'F',op_flags=['readwrite']):
    row[...] = row * row

# getting the output here
print("Array after making some changes in it at the runtime : \n" + str(a1))

a2 = np.arange(12).reshape(3,4)

# iteration over to 2 arrays simultanously
for x,y in np.nditer([a1,a2]):
    print(x,y,end = ' ')
print()