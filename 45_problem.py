class object:
    a = 9


obj = object()
print(obj.a)  # this will print the class variable value as instance variable is not present

obj.a = 0  # Instance attribute is created
print(obj.a)  # this will print the instance variable value as instance variable is present but note that it is not changing the class variable 

# if we print the class variable we will see that it is not updated
print(object.a)



