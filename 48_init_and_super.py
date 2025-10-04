# Multiple Inheritance with __init__ and super() 

class Person:
    def __init__(self):
        print("Person initialized")

# this will make multi level inheritance when student is passed to scholar
class Student(Person):
    def __init__(self):
        super().__init__()
        print("Student initialized")

class Player(Person):
    def __init__(self):
        super().__init__()
        print("Player initialized")

# Python checks from left to right in the class declaration
class Scholar(Student, Player):
    def __init__(self):
        super().__init__()
        print("Scholar initialized")

s = Scholar()
print(Scholar.__mro__)  # To see how Python decides which parent to call: