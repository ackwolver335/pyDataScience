"""
    Getting Started with Dictionary and Tuples : 
    1. Dictionary's Definition : 
    Dictionary : It is a particular type of data type that stores data in the form of key : value pairs, and also sometimes these are called as Maps, Hashables, and Associate Arrays.

    Syntax : dictionary_name = {"Key_name" : ValueHere,"Key2":Value}

    Tuple's Introduction :
    >> Tuple is a list of values that are grouped together and can not be changed once the values are assigned to it.
    >> Values in the tuples have different meaning therefore these are considered as Heterogeneous and lists are homogenous as the values of them are similar.
    Syntax : tup_name = (value1,value2)
"""

# creating a dictionary here
dict1 = {"tel1" : 23423423,"tel2" : 234223234,"tel3" : 34857398754}
print(dict1)

# accessing the elements regarding it
print(dict1["tel2"])

# adding a new element in the dictionary
dict1["tel4"] = 3484858734

# checking the order of the dictionary after adding a new element
print(dict1)

# deleting an entry from the dictionary
del dict1["tel3"]
print("Elements after deleting one key value pair from the dictionary : " + str(dict1))

# printing all the values from the dictionary
for key in dict1:
    print("Key : " + str(key) + " | Value : " + str(dict1[key]))

# checking if a particular item is available in the dictionary
if "tel1" in dict1:
    print("Telephone 1 is available in the dictionary !")
else:
    print("No the value is not present in the dictionary !")

# deleting the entire dictionary's elements
dict1.clear()
print("Dictionary after clearing all data is : " + str(dict1))

# creating a tuple here
points = (3,4,5,6)                              # coordinates of the line

# accessing the data in the similar way that we use for lists
print("First element of the Tuple is : " + points[0])

# Tuples are immutables and can't be changed in its values once it is assigned.