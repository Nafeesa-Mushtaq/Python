# remove the given word from the list and strip it at the same time 

# strip is a function which is used to remove the specific characters from the given word from begining as well as from end
# lstrip() is used to remove left side of the word and rstip is used to remove from right side of word


def rem(list, word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n
    
l = ["Nafeesa", "Amna", "Alina", "Ruksana", "Shabana", "na"]

print(rem(l,"na"))
