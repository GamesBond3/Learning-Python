import random
'''
1 for Rock
0 for Paper
-1 for Scissor

'''

Computer_choice = random.choice([1, 0 ,-1])

Player_input = input("Enter your Choice: ")
Player_dict = {"Rock" : 1, "Paper" : 0, "Scissor" : -1}
Reverse_Player_Dict = {1 : "Rock", 0 : "Paper", -1 : "Scissor"}

Player = Player_dict[Player_input]

print(f"You chose {Reverse_Player_Dict[Player]} \nAnd Computer chose {Reverse_Player_Dict[Computer_choice]}")

if(Computer_choice == Player):
    print ("It's a tie")
else:
    if(Computer_choice == 1 and Player == -1):
        print("Computer Won!")
    elif(Computer_choice == 1 and Player == 0):
        print("You Won!")
    elif(Computer_choice == 0 and Player == 1):
        print("Computer Won!")
    elif(Computer_choice == 0 and Player ==-1):
        print("You Won!")
    elif(Computer_choice == -1 and Player == 1):
        print("You Won!")
    elif(Computer_choice == -1 and Player == 0):
        print("Computer Won!")
    else:
        print("Something Went Wrong")