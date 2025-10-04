from random import randint

n = randint(1,100)
# print("Computer entered: ",n)
temp = 1
u = -1

# for i in range(1,1000):
#     u = int(input("Enter the number to guess: "))
#     if(n < u):
#         print("Enter lower number please")
#         temp += 1
#     elif(n > u):
#         print("Enter higher number please")
#         temp += 1
#     elif(n == u ):
#         print("Right you Gussed it")
#         temp += 1
#         break

# print(f"You have gussed the number {n} in {temp} attempts")


# NOTE that it is more efficint and clean with while loop 
while(u != n):
    u = int(input("Enter the number to guess: "))
    if(n < u):
        print("Enter lower number please")
        temp += 1
    elif(n > u):
        print("Enter higher number please")
        temp += 1

print(f"You have guessed the number {n} in {temp} attempts")