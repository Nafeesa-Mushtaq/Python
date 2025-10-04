f = open("File.txt")

# this will return the list of all lines present in the file
data = f.readlines()  
print(data)

# this will read line until it finds a new line or end of the file --- in short it will read one line only when called and in oder to read more lines you have to call it again

# rb --- read file in binary mode    rt --- read file in text mode 
# d = f.readline()
# print(d)

f.close()