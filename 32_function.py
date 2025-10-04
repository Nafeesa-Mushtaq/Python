
# functions are useful to reuse the logic

# function defination
def average():
    a = int(input("Enter No 1: "))
    b = int(input("Enter No 2: "))
    c = int(input("Enter No 3: "))

    average = (a+b+c)/2
    # print is a built in function while average is user define function
    print(f"The average of {a} , {b} , {c} is : {average}")


for i in range(1,6):
    average()  # function call