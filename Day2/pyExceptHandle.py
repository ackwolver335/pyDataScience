"""
    Getting started with Exception Handling in Python :
    1. Exception : It is the one error or bug that you didn't expect from your code but it happens here.
    2. Handling Exception : Action of taking changes in your code previously at that particular stage where you could surely found or have an idea
    about that, at that particular line of code any particular error may occur.

    Note : A Major benefit of exception handling is that we can easily save our programs from crashing through the exceptions that occurs 
    unconditionally in our python programs.

    # As we can't directly divide 1 to 0 it will provide us error
    # 1/0
    # Similarly we can't directly add a number to the string it will also provide us error
    # 'name' + 23
"""

# taking division of two numbers
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

"""
    # Basic Level Execution
    division_value = num1 / num2                                        # here any exception may occur
    print("Value after division is : " + str(division_value))           # if there is any error in the division this line will not be executed
"""

# Handling the Above Exceptions
try:
    # code below may have exception here
    division_value = num1 / num2
    print("Division value is : " + str(division_value))
except Exception as e:
    print(e)                                                    # occured exception will be printed here

# Handling specific exception
try:
    division_value = num1 / num2
    print("Division value : " + str(division_value))
except ZeroDivisionError as e:
    print("Zero Division Exception : Given number can't be divisible by zero !")

# Handling Multiple Exceptions
try:
    division_value = num1 / str(num2)
    print("Division value : " + str(division_value))
except ZeroDivisionError as e:
    print("Zero Division Error here !")
except TypeError as e:
    print("Type Error Exception ")