# To see how super() works in deep chaining of inheritance
# remeber that compiler execute the code line by line

class A:
    def info(self):
        print("Info from A")

class B(A):
    def info(self):
        super().info()
        print("Info from B")

class C(B):
    def info(self):
        print("Info from C")
        super().info()

class D(C):
    def info(self):
        print("Info from D")
        super().info()

d = D()
d.info()
print(D.__mro__)  # To see how Python decides which parent to call: