# Returns a new dictionary that merges both, without modifying originals.

a = {'x': 1, 'y': 2}
b = {'y': 100, 'z': 200}

c = a | b
print(c)  # {'x': 1, 'y': 100, 'z': 200}
