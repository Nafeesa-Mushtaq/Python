# sum of the numbers using recursion 

def sum(n):
    if(n == 0):
        return 0
    return (n + sum(n-1))

i = int(input("Enter the number of which you want the sum : "))

print(f"The sum of {i} is {sum(i)}")