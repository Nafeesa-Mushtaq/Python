# as we know set is a collection of well defined objects, it cannot contain repeating elements it contains only distinct elements
s = {1,2 ,3 ,4}

# we cannot make s = {} as empty set as it will creat as empty dictionary , this is how the empty set can be made
e = set()

# if we place repeating elements in the set, then on printing it will not repaeat them 
# one imp point here is that set do not maintain the order, if you want to maintain the order you should use list

s = {1,2,3,4,1,3,55}
print(s)
