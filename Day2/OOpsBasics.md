# 🖥️ Basics of OOPs in Python 🐍

🎯 **What is a Class** ❓

➱ A class is an abstraction of some entity which contains common set of properties and methods.

🎯 **Define Object** ❓

➱ An Object is nothing but a specific instance of a **Class** that contains the structure of the class for working over to it.

Example : **Tom Cruise** and **Maria Sharapova** both have a name, gender and Occupations but are different as and when compared with the help of their methods or the work they do or are known for.

## 🖱️ Creating a Class 📑

▷ Below we have the syntax for creating **Classes** in Python and also together by this we'll be surely creating the instances of the classes.

```python
class Class_name:

    # specific class method for initiating properties of the class
    def __init__(self,arg1,arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    # defining some other method
    def getArgs(self):
        print("First Argument is : " + str(self.argument1) + "\nSecond Argument is : " + str(self.argument2))
```

## ⌨️ Creating an Instance of Class 🕹️

⦿ Below we have an example regarding instance of class that we have created above.

```python
object1 = Class_name(23,45)
object1.getArgs()
```