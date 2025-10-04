# sets are unordered they do not maintain the order 
# we cannot access the set elements using index
s = {1,2,3,"Nafeesa",78}
p = {1,4,2,5,3,6,78}

# this is use to add something to set
s.add("Alina")

print(s,type(s))

# it will remove the element from the set
s.remove(1)

# it will remove a random element from the set
s.pop()

# this is will clear the set
# s.clear()

# this will give the union of the two sets
print(s.union(p))

# this will give the intersection of two sets
print(s.intersection(p))

# this will give the difference of the sets
print(s.difference(p))




# we can learn more methods from chatGPT