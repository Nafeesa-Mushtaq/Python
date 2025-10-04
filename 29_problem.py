'''
    *
   ***
  *****
 *******
*********

'''

n = int(input("Enter the number of stars: "))

for i in range(1, n + 1):
      # print by default gives a new line but when we write
        print(" "*(n-i),end="") 
        print("*"*(2*i-1), end="")
        print("")

print(" ")

# now by using nested loop
for i in range(1, n + 1):
    # Print spaces
    for space in range(n - i):
        print(" ", end="")
    # Print stars
    for star in range(2 * i - 1):
        print("*", end="")
    # Move to next line
    print()

         
