import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')

#main loop of the game
def main():
    print("Rock, Paper, Scissors")
    userInput = input("What will you choose? [R]ock, [P]aper, [S]cissors?: ")

    print("\n")

    #setting the options for the AI to choose from
    options = ['Rock', 'Paper', 'Scissors']
    AIChoice = random.choice(options)
    print("Opponent chose", AIChoice)
    
    #changes lowercase inputs to uppercase
    str.upper(userInput)

    #changes single letter to full word
    if userInput == 'R':
        userInput = "Rock"
    elif userInput == 'P':
        userInput = "Paper"
    elif userInput == 'S':
        userInput = "Scissors"
    #tells user their choice
    print("You chose",userInput)

    #places all possible choices where user wins
    if userInput == 'Rock' and AIChoice == 'Scissors':
        print("Rock beats scissors, you win")
    elif userInput == 'Scissors' and AIChoice == 'Paper':
        print("Scissors beats paper, you win")
    elif userInput == 'Paper' and AIChoice == 'Rock':
        print("Paper beats rock, you win")
    
    #Scenarios where its a tie or user loses
    elif userInput == AIChoice:
        print("It's a tie")
    else:
        print(AIChoice,"beats", userInput,". You lose")

main()
