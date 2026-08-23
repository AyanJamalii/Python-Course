import random

'''
-1 = Paper
0 = Rock
1 = Scissor
'''

computer = random.choice([1, 0, -1])
youstr = input("Enter your Choice: ")
youDict = {"p" : -1, "r" : 0, "s" : 1}
reverseDict = {-1 : "Paper", 0: "Rock", 1: "Scissor"}
you = youDict[youstr]

print(f"You Choosed {reverseDict[you]} and Computer Choosed {reverseDict[computer]}")

if computer == you:
    print("Its a Draw.")
else: 
    if computer == -1 and you==1:
        print("You WIN!!")
    elif computer == -1 and you == 0:
        print("You Lose!")
    elif computer == 0 and you == -1:
        print("You WON!!")
    elif computer == 0 and you == 1:
        print("You Lose!")
    elif computer == 1 and you == 0:
        print("You WON!!")
    elif computer == 1 and you == -1:
        print("You Lose!")
    else: 
        print("Something Went Wrong.")
