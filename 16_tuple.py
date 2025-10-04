# tuple is just liske list except the fact that tuple is immutable like stings

a = (1,3,55,6,677,88,66,88, "Ali", "Ahmed")

# empty tuple
b = ()

# tuple with single value --- makesure to put the comma otherwise python will treat it as int
c = (1,)

# a[0] = 456 is wrong as it is immutable

# this will tell how mnay times a value exists in the tuple
no = a.count(88)
print(no)

# this will return the indux of the first occuring value in the tuple 
no = a.index(88)
print(no)

# you can learna about tuple methods from chat gpt
# learn about tuple unpacking
