# Everthing in python is a class even integar string all are the classes
# Operators like + - can be overloaded in pyhton using dunder (__name__) methods and these dunder methods are called when operators are used on objects

class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        return self.n + num.n

n = Number(1)
m = Number(12)

# this will give error if add function is not present
print(n + m)


'''
Operator overloading means giving custom meaning to Python operators (+, -, *, ==, etc.) for user-defined classes.

For example:

Normally, + adds numbers.

But with operator overloading, you can define what + should do for your own class, like adding two Person or Point objects.

'''

'''
Operator	    Method Name
+	            __add__()
-	            __sub__()
*	            __mul__()
==	            __eq__()
/               __truediv__()
//               __floordiv__()
<	            __lt__()
>	            __gt__()
len(obj)        __len__()
'''