import random, time, os, sys

# clears the console screen
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# give countdown and receive user's selection
def getUsersChoice(options):
    input("\nJust let me know when you're ready. (press any key)\n")

    for i in range(3):
        print(options[i] + "...")
        time.sleep(0.5)
    print("\nShoot!!")

    return input().lower().strip()

# checks if user's choice is valid, and chides them if not
def choiceIsValid(user_choice, options):

    # check how many choices match user's selection
    matches = [option for option in options if option.startswith(user_choice)]

    if len(matches) == 1:
        # if user's selection matches exactly one potential choice return true
        return matches[0]
    
    else:
        # if user's choice does not match exactly one, then chide them and return false
        print("\nOkay, very funny. You know the options... This time why don't you play right, eh?")
        print("You know, by choosing... rock, paper, or scissors? Duh! It's in the name of the game!.")

        return False
    
# TODO:implement more complex logic for computer selection: e.g. difficulty levels, cheating,
# prediction methods, user-specific strategies, opponent playstyle recognition, etc."""
def getComputerChoice(options):
    return random.choice(options)

def rps():
    # initialize the list of options in this game
    options = ["rock", "paper", "scissors"]

    # play a round, loop through user choice logic until a valid choice is made
    validChoice = False

    while validChoice is False:
        # get users selection and check choice is valid and store the valid choice
        validChoice = choiceIsValid(getUsersChoice(options), options)
    
    print("\nYou chose: " + validChoice)

    # Generate computer's choice
    print("I chose: " + (computer_choice := getComputerChoice(options)) + "!!\n")

    # Determine winner
    if validChoice == computer_choice:
        print("It's a tie!")
    elif (validChoice == "rock" and computer_choice == "scissors") or \
         (validChoice == "paper" and computer_choice == "rock") or \
         (validChoice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

# main game loop
while True:

    # welcome user and introduce game
    clearScreen()

    print("Hey, nice to see you!")
    print("\nLooks like you want to play a game of Rock, Paper, Scissors, eh? I'm down.")
    print("It's a very simple game, so I'll assume you know what you're doing here.")

    # initate game logic
    rps()

    # ask to play again
    play_again = input("\nPlay again? (y/n): ")

    # if done playing, say goodbye and close game
    if not play_again.lower().startswith("y"):
        input("\nWell, that was fun! See you around. (press any key)")
        clearScreen()
        break