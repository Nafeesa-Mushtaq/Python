# The reduce() function is used to repeatedly apply a function to a sequence, reducing the sequence to a single value (e.g., sum, product, max, etc.).

# Syntax
# from functools import reduce
# reduce(function, iterable, initializer)
# This is how it works --- ((((a1, a2), a3), a4), ...) → single value

from functools import reduce

nums = [1, 2, 3, 4]

total = reduce(lambda x, y: x + y, nums)
print(total)

