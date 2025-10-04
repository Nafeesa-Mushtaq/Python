# squares = []
# for x in range(1, 11):
#     if x % 2 == 0:
#         squares.append(x**2)

# print(squares)


# The same can be done using list compreshensions
squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares)
