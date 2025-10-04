# It's used to assign a value to a variable inside an expression, like inside an if, while, or list

# NOTE without warlus

n = input("Enter something: ")
if n != "":
    print(f"You entered {n}")


# NOTE with warlus 
if (n := input("Enter something: ")) != "":
    print(f"You entered {n}")
