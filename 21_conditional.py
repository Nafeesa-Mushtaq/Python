a = int(input("Enter your age: "))

# remember the syntax and also that the space is important after if else just like dry run

if(a>18):
    print("You can drive")
else:
    print("you can not drive")


# if we have to write multiple if else as we do in c or java we will write elif instead of elseif
b = int(input("Tell me your experience: "))
if(b<2):
    print("You can work as office boy")
elif(b>2 and b<5):
    print("You can work as casiher")
elif(b>5 and b<10):
    print("You can work as accountant")
else:
    print("you can have a higher post")