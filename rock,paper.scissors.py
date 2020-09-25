from random import randint

#create a list of player options
choices = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = choices[randint(0,2)]

#set player to False
player = False

while player == False:

    player = input("Rock, Paper, Scissors?").capitalize()
    if player == computer:
        print("It's a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("Computer win!")
        else:
            print("Player win!")
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer win!")
        else:
            print("Player win!")
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer win!")
        else:
            print("Player win!")
  
    # we want it to be False so the loop continues
    player = False
    computer = choices[randint(0,2)]


    #kjgf