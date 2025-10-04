d = {}  # this is empty dictionary 
print(type(dict))
marks = {
    "Nafeesa": 24,
    "Noor"   : 25,  
    "Ayesha" : 23,  
}

# it will print all the key value pais of the dictionary in the form of tuples
print(marks.items())

# this will return the keys of dictionary
print(marks.keys())

# this will give the values of all keys
print(marks.values())

# this will update the value of corresponding key --- we can also add new key value pais using update() method  --- remember to keep the syntax same
marks.update({"Nafeesa" : 100})


# this will return the values of the key
print(marks.get("Ayesha")) # this may look similar to marks["Ayesha"] but the key difference between them is that if the key does not exist in the dictionary, get method will return NONE while the [] syntax will give an error that is why both are not same  -- for example

# print(marks["Hadi"])     #this will give an error
print(marks.get("Hadi")) #this will output as None

# LEARN MORE METHODS FROM CHATGPT
