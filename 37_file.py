
# this is used to open the file just place the name of the file inside the function if it is present in the same directory otherwisw place the location
# open(path,mode)
#  r -- read  w -- write  a --- append  r+ -- read + write  w+ --- write + read  a+ -- appeand + read
# by deafult it will be opened in the read mode
f = open("file.txt")
data = f.read()
print(data)
f.close()