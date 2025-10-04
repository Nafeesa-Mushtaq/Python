# Multiple Inheritance with super() in Methods  

class Father:
    def show(self):
        print("Father's show")

class Mother:
    def show(self):
        print("Mother's show")

# this have now access to all attributes and methods of base classes
class Child(Father, Mother): #python satrts calling from left to right
    def show(self):
        print("Child's show")
        super().show()  # Calls Father's show because of MRO

c = Child()
c.show()
print(Child.__mro__)   # To see how Python decides which parent to call:
