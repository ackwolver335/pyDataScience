"""
    Getting started with If Statement
    1. using its structure and usage procedure.

    Syntax for if statement : 

    if condition:
        # code here to be executed if the condition gets true

    else:
        # code to be executed if the condition gets false

    Further more we can use different operators regarding it like <,>,<=,>= and any more regarding numerical operations

    # Elif statement usage for multiple condition's check
    if condition:
        # code here
    elif condition:
        # code here
    elif condition:
        # code here
    else:
        # code here
"""

# Sample Problem : WAP that asks user to enter a number, Program should tell if the number is odd or even.
number = int(input("Enter a number : "))                                    # converted into a number using int()

if number%2 == 0:
    print("The given number is Even !")
else:
    print("The given number is Odd !")

# Sample Problem : WAP that asks user to enter dish name and it should print which cuisine is that dish of.

indian_cuisine = ["samsosa","daal","naan"]
chinease_cuisine = ["egg role","pot sticker","fried rice"]
italian_cuisine = ["pizza","pasta","risotto"]

dish = input("Enter a dish name : ")
if dish in indian_cuisine:
    print("Dish is Indian")

elif dish in chinease_cuisine:
    print("Dish is Chinease")

elif dish in italian_cuisine:
    print("Dish is Italian")

else:
    print("Based on little amount of data I m unable to identify the dish category")