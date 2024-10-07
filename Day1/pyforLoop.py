"""
    Getting Started with for Loop or Looping Statements

    Syntax :
    for items in iterable_variable:
        # code here

    Note : So, the for  loop is used when we need to work or perform particular operation on a number of iterable items

    While Loop Syntax :

    initiating_var = 0
    while condition:
        # code here
        # stopping condition code
"""

# Sample Problem : WAP that store your monthly expenses in a list and find out total expenses for all months
expenses = [2230,5000,3422,5043,3100,2300]

"""
    Wrong way to do that or time taking unoptimized procedure
    total = total[1] + total[1] + total[2] + total[3] + total[4]
"""

# doing that with the right way
total = 0

# Correct way to do that
for values in expenses:
    total += values

print("My Total Expenses is : " + str(total))       # getting the sum of total in output

# Using range() method for getting a iterable as per the given values
for i in range(1,11):
    print(str(i) + " ",end = " ")

print()

# printing the monthly expenses here
for i in range(len(expenses)):                      # using len() method to pass the list length for range() method ending index value
    print("Month : " + str(i + 1) + " Expenses : " + str(expenses[i]))

# using while loop
i = 1
while i < 5:
    print(str(i) + " ",end = " ")
    i += 1

print()