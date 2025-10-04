
# recurssion says that a function calls itself in itself --- best example is factorial
# NOTE that there must be a condition to end the recursion otherwise it may lead to infinite dunction call

n = int(input("Enter the number of which you want the factorial: "))
def factorial(n):
    if (n== 1 or n == 0):
        return 1
    return n*factorial(n-1)

print(f"The factorial of {n} is {factorial(n)}")

