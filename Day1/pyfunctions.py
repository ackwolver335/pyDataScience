"""
    Getting started with Python Function or Methods

    Intro : Function is a particular block of code that is been used in order to perform a particular task a number of times without writing the code again and again

    Syntax for functions :

    def function_name(args,..):
        # code here
        return value                        # functions ends where we use the return statement

    1. Arguments : Values that are passed at the time of calling a function.

    i. Positional Args : Values passed as per the required position asked as per function's definition
    ii. Named Args : Passing the arguments as per the name of arguments that are passed here.
    iii. Default Arguments : Arguments values that are defined at the function's definition for a chance if the values are default at there.
"""

# Sample Problem : You are given two lists of numbers and you need to find total of each of these lists.
list1 = [2100,3400,3500]
list2 = [200,500,700]

total = 0

"""
    Problem : Here we have used the code again and again and this is that's why not the right way to use the code

    # total of list1
    for item in list1:
        total += item

    print("The total of first list : " + str(total))

    total = 0

    # total of list1
    for item in list2:
        total += item

    print("The total of first list : " + str(total))
"""

# creating a function here
def cal_total(exp):

    """
        Documentation String for providing about a particular function's or program that what the program or 
        methods is created for !
    """

    total = 0

    # iterating through lists here
    for items in exp:
        total += items
    
    return total

# getting the total or lists now
total_list1 = cal_total(list1)
total_list2 = cal_total(list2)

print("Total of first list : " + str(total_list1))
print("Total of second list : " + str(total_list2))

# using named arguments
def sum(a=2,b=2):
    return a + b                # it will also work if we don't have that particular argument's passed