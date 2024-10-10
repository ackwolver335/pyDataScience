"""
    Getting started with the Concept of __name__ == __main__ :

    This particular thing is used as an entry point for a particular python program, and is similar to the main() method of other programming
    languages like C++ or JAVA.

    On importing, the value regarding it, the value of __name__ becomes the name of the module that is been imported
"""

# getting the value of __name__
print(__name__)

# defining a method here
def getSum(a,b):
    if __name__ == "__main__":
        print("__name__ : ",__name__)
        return a + b

# calling the method here only first
getSum(4,5)