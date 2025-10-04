n = input("What is your name: ")

# this is the function with arguments but with no return value
def greet(name):
    print("Good morning!",name)

greet(n)

# this is the function with return value 
def average():
    a = int(input("Enter No 1: "))
    b = int(input("Enter No 2: "))
    c = int(input("Enter No 3: "))

    average = (a+b+c)/2
    # print is a built in function while average is user define function
    print(f"The average of {a} , {b} , {c} is : {average}")
    return average

a = average()

print(f"{a} is returned from the function")


# in this function end is given a default value, if we dont pass both the arguments it will give error but if you pass the argument it will ignore the default value and consider the passed value
def greeting(name, end= "Welcome"):
    print("Good morning!",name)
    print(end) #here bye will be printed instead of welcome


greeting(n,"Bye")
