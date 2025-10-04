
# this will skip the iteration of the loop
for i in range(20):
    if(i%2 == 0):
        continue
    print(i)

# this will exit the loop immediately
for i in range(10):
    if(i==7):
        break
    print(i)

# the else will not execute when the loop is skipped it will execute only when the loop ends
for i in range(10):
    if(i%2 == 0):
        continue
    print(i)
else:
    print("Skipped")