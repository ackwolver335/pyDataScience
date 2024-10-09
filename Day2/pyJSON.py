"""
    Getting started with JSON files : 

    Tasks in the form of Programs : 
    1. To create an address book and write some records in it
    2. Read this address book
"""

# importing the required module in order to dump the Book into JSON format
import json

# creating a dictionary as a JSON Object
book = {}

# adding data elements to the dictionary
book['Ack'] = {
    'name' : 'Ack Wolver',
    'address' : 'New York City, Street No. 10A',
    'phone' : 935921893
}

# adding some more elements to it
book['Stelon'] = {
    'name' : 'Stelon Mark',
    'address' : 'Stugyard, Europe',
    'phone' : 92349231
}

s1 = json.dumps(book)               # here we have dumped the Book and its data into a JSON Format
print(s1)

# Now let us write this to a particular file
"""
    with open("/home/ackwolver/Documents/GithubData/DataScience/Day2/book.json","w") as file:
        file.write(s1)
        file.close()
"""

# Now let us try reading the data after opening the file
f1 = open("book.json","r")
file_data = f1.read()
print(file_data)

# loading string with the help of JSON Format
loaded_data = json.loads(file_data)
print(loaded_data)

# you can try printing the data elements as the loaded_data is now a dictionary