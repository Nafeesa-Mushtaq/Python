# init is also called the constructor of the class

# NOTE that only ONE  __init__ is allowed per class , in contrast to java constructor overloading is not allowed in python

class Person:
    address = "abc "
    name = "xyz"

    # this is how we write constructor in python
    # In python the methods which start from double underscore are called dunder method
    # Also called as magic method

    def __init__(self):
        print("Hello I am init function and i work just like a constructor in the java language and you dont have to call me manually, i will be called automatically when the instance if the class is created")

    # NOTE that we cannot create spearate constructors in python like in java
    def __init__(self,address,name):
        
        self.address = address
        self.name = name
        print(f"This is my init function with argument so that we can assign the names to the variables directly while creating the instance")


Fatima = Person("Jhang","Nafeesa")


    