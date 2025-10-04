'''
f = open("file.txt")
print(f.read())
f.close()

'''


# the same as above lines can be written with the help of " with statement"
with open("file.txt") as f:
    print(f.read())

# NOTE we dont have to explicitly close the file 