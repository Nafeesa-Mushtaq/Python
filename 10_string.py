
# we can write the string in single, double and triple quote
str1 = "Nafeesa"
str2 = 'Nafeesa'
str3 = '''Nafeesa'''

# strings are imputeable 
# we can find the length of the string using len()
# we can slice the string by using its index


str4 = len(str1)  # this will give the length of the string

str5 = str1[0:3]  # this says that start from 0 and end before 3
str6 = str1[3]    # this says that put the index 3 'e' in it

# there is also something called negative slicing , in this we give the last letter -1 and -2 and soo on

# this means it is starting from 0 and ending before length - 1 
str7 = str1[:]

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)

