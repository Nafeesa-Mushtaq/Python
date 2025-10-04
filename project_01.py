'''
Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.

'''

import random

Choice = ["Water","Gun","Snake"]
cmp_score = 0
user_score = 0


def call():
    global cmp_score, user_score 
    user = input("Enter your choise: ")
    cmp = random.choice(Choice)
    print(f"The computer choose {cmp} and You choosed {user}")

    if(cmp.lower() == user.lower()):
        print("Its a Draw!")

    else:
        if((cmp.lower() == "water" and user.lower() == "gun" ) or (cmp.lower() == "gun" and user.lower() == "snake" ) or (cmp.lower() == "snake" and user.lower() == "water" )):
            print("You Loss 🥺😢! Try again")
            cmp_score += 1

        elif((user.lower() == "water" and cmp.lower() == "gun") or (user.lower() == "gun" and cmp.lower() == "snake") or (user.lower() == "snake" and cmp.lower() == "water") ):
            print("You win 🥳🎊")
            user_score += 1

    

for i in range(1,6):
    call()


print(f"After completing the round, Computer has score {cmp_score} and You have {user_score}")

if(cmp_score == user_score):
    print("It is a Draw")

elif(cmp_score > user_score):
    print("Computer won! You loose")

else:
    print("You Won")
    