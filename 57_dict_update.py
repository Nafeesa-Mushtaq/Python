# Modifies the original dictionary by adding/updating key-value pairs from another dictionary.
a = {'x': 1, 'y': 2}
b = {'y': 100, 'z': 200}

a.update(b)
print(a)  # {'x': 1, 'y': 100, 'z': 200}
