
n = input("Enter whatever you want to write in the file: ")

f = open("myFile.txt" , "w")
f.write(n)
f.close()

