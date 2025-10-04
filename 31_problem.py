# reverse loop for printing the reverse table

n = int(input("Enter the number of which you want the table: "))

for i in range(1,11):
    # the logic is reversed here 
    print(f"{n} x {11-i} = {n*(11-i)}")