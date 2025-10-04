# property method works just like getters in java

class Circle:
    def __init__(self, radius):
        self._radius = radius  # underscore → treated as "private"

    # works like getter to access the private variable
    @property
    def area(self):
        return 3.14 * self._radius * self._radius

    @property
    def radius(self):
        return self._radius

    # this will work like a setter to set the value of the private variable
    @radius.setter
    def radius(self, value):
        if value < 0:
            print("Radius can't be negative.")
        else:
            self._radius = value


c = Circle(5)

print(c.area)       # Access like an attribute → 78.5
print(c.radius)     # 5

c.radius = 10       # Calls the setter
print(c.area)       # 314.0

c.radius = -4       # Triggers validation


#                       NOTE Example 02

class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return self.ename

    
    @name.setter
    def name(self,name):
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]
    
     
e = Employee()
e.name = "Amal Nayyab"
print(e.fname , e.lname)

e.show()