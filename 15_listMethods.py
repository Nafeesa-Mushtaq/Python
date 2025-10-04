friends = ["apple", "banana", 23, 45.9 , "sania" , "Nafeesa"]
print(friends)

# this will change the original list unlinke the string and add at the end of list
friends.append("Meer Hadi")
print(friends)

l1 = [1 , 3 , 5 ,2 , 5 , 8 , 7 , 12 , 10 , 4 ]

# this will sort the list in ascending order
l1.sort()
print(l1)

# this will sort it in decesending order
l1.reverse()
print(l1)

# this will remove the item from the list
l1.remove(2)
print(l1)

# this will insert 333 at the index 2
l1.insert(2,333)
print(l1)

# this will delete the elemnt from list and return the value
l1.pop(2)
print(l1)