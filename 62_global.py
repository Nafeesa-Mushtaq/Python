x = "outside"

def change():
    global x
    x = "inside"

print(x)  # outside
change()
print(x)  # inside
