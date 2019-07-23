import random          # imports the library named random
def rps():
    user = input("Choose your weapon: ")
    comp = random.choice(['rock','paper','scissors'])
    print()

    print('The user (you) chose', user)
    print('The computer (I) chose', comp)
    print()

    if user == comp:
        print("It's a tie")
    elif user == "rock" and comp == "paper":
        print ("HAH! I win this round.")
        print("Better luck next time...")
    elif user == "rock" and comp == "scissors":
        print("You win this round!")
    elif user == "paper" and comp == "rock":
        print("You win this round!")
    elif user == "paper" and comp == "scissors":
        print ("HAH! I win this round.")
        print("Better luck next time...")
    elif user == "scissors" and comp == "rock":
        print ("HAH! I win this round.")
        print("Better luck next time...")
    elif user == "scissors" and comp == "paper":
        print ("You win this round!")
    else:
        print("Not a valid input")
        print("Check your spelling!")
