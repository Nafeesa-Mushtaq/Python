# Class and its objects

class Employee:
    comapny = "abc" # class attribute
    salary = 120000


# Fatima is the object of the class
Fatima = Employee()
Fatima.name = "Fatima" # this is the instance attribute (attribute of object or instance of the class)
Fatima.salary = 100000 # now we have redefind the attribute --- on printing it will show 10000 instead of 120000 as the compiler will first check the attribute in instance of class if present than use it if not than check to the class 
print(Fatima.comapny)    # this is the class attribute