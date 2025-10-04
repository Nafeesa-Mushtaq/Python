
# The map() function allows you to apply a function to every item in an iterable (like a list) and returns a new iterable (a map object, usually converted to a list).

def square(x):
    return x ** 2

nums = [1, 2, 3, 4]
squared = list(map(square, nums))
print(squared)


# Another Example
names = ['noor', 'ayesha', 'amna']
uppercased = list(map(str.upper, names))
print(uppercased)

# NOTE map() returns a map object, so you usually wrap it with list() to see the result.