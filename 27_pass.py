
# PASS is a null statement in python which instructs to "do nothing"
# just take an examole if you want to work first on a problem while the one you are already working upon in not completed simply write the pass

l = [1,2,3,4,5,6,"Nafeesa"]
for i in l:
    pass   # without pass the program will thorw an error
# now i can work on the lower loop whitout completing the upper one as pass is allowing us to do so as it will not cause any error due to pass 


for i in range(10):
    if(i==7):
        break
    print(i)