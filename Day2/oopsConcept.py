"""
    Getting started with the Concept of OOps :
    1. Creating a class
    2. Creating instance of the class
"""

class Human:        # class with name "Human"

    # specific method used in order to intialize the properties of the class
    def __init__(self,n,o):
        self.name = n
        self.occupation = o

    # defining some methods for specific purpose
    def do_work(self):
        if self.occupation == "tennis player":
            print(str(self.name) + " plays tennis")
        else:
            print(str(self.name) + " used to shoot films")

    # another method for speaking
    def speak(self):
        print(str(self.name) + " speaks english !")

# creating an instance/object for the class
tom_cruise = Human("Tom Cruise","Actor")
tom_cruise.do_work()
tom_cruise.speak()

# creating another instance of the class
maria = Human("Maria Sharapova","tennis player")
maria.do_work()
maria.speak()