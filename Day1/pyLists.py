# let's get started with lists
item1 = 'Bread'
item2 = 'Fruits'
item3 = 'Vegetables'
item4 = 'Pasta'

# for doing that at a particular container we uses a list
items = [item1,item2,item3,item4]                               # this is a new helpful component from the side of Python

"""
    We did the same things here regarding the one with the required one.
"""

items_index = [0,1,2,3]             # these are the index regarding the one we need to work on
print("Accessing the first item here : " + items[0])

# changing the data in the list
items[2] = "Banana"

print("Getting the data from the indexes : "  + items[1] + " " + items[-2])         # using negative indexing

# adding an item in the list at a specific position
items.insert(2,"Apple")                                                             # apple will be added at third position

# creating another list for food items
food = ["bread","potata"]
all_Items = items + food                        # it will join these two lists together here

# printing the data to check
print(all_Items)

# Remember that we can not add items directly to the lists : items + "Data1"
# getting the length of the list
print(len(all_Items))

# checking if the a particular elements is present in the list or not
print("Pasta" in all_Items)