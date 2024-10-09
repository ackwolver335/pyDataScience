"""
    Getting started with the concepts of Modules :
    Syntax : import module_name

    for importing module from specific location in your Device
    import sys
    sys.path.append('file_location_here')
"""

# importing math module here for importing concept
import math
import calendar

# using a particular math module method or function
print("Square root of 4 is : " + str(math.sqrt(4)))

# getting the details regarding all the methods or functions available in math module
print(dir(math))

# Note : For getting more details regarding you may google the details regarding it
# some other methods regarding this
print(math.pi)
print(math.log10(100))
print(math.floor(2.5))

cal = calendar.month(2016,1)
print(cal)

# checking if the next year 2025 is a leap year or not
print(calendar.isleap(2025))

# creating our own methods here for creation of custom python methods
def getSum(a,b):                                                                # method for getting sum of two numbers
    return a+b

def getProduct(a,b):                                                            # method for getting product of two numbers
    return a*b

# Note : We can also overtake any particular module from a particular location in your Device as per the syntax
# given at the starting of this file