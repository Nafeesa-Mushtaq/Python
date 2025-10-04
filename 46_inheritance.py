# Base class
# NOTE that base class cannot access the derived class attributes but derived clas can access the base class attributes
class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the comapny is {self.company} and the name of employee is {self.name}")

# Derived class
# This is how we perform inheritance in python
# we can access the attributes of base class in the derived class
class Programmer(Employee):
    def language(self):
        print(f"The employee {self.name} is working in {self.company} in language {self.lang}")

a = Employee()
a.name = "Nafeesa"
b = Programmer()
b.name = "Amal"
b.lang = "Python"

a.show()
b.show()
b.language()