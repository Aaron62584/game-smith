import random
import time
from collections import defaultdict
from gsclasses import Player
from gsutilities import clear_screen

def get_computer_choice(options):
    """get computer choice"""
    # TODO:implement more complex logic for computer selection:
    # e.g. difficulty levels, cheating, prediction methods, user-specific
    # strategies, opponent playstyle recognition, etc.
    return random.choice(options)

def get_user_choice(options):
    """give countdown and receive user's selection"""
    valid_choice = False
    
    while not valid_choice:
        input("\nJust let me know when you're ready. (press enter)\n")

        for i in range(3):
            print(f"{options[i]}...")
            time.sleep(0.5)
        print("\nShoot!!")

        valid_choice = choice_is_valid(input().lower().strip(), options)
    
    return valid_choice

def choice_is_valid(user_choice, options):
    """checks if user's choice is valid, and chides them if not"""
    # check how many choices match user's selection
    matches = [option for option in options if option.startswith(user_choice)]

    if len(matches) == 1:
        # if user's selection matches exactly one potential choice return true
        return matches[0]
    
    else:
        # if user's choice does not match exactly one, then chide them and
        # return false
        print("\nOkay, very funny. You know the options... This time,")
        print("why don't you play right, eh? You know, by choosing... rock,")
        print("paper, or scissors? Duh! It's in the name of the game!.")

        return False

def create_graph():
    """create directed graph"""
    #TODO: make directed graph configurable, durable and user-specific. also
    # implement validation logic. maybe make the graph an object with method
    # calls to alter options and win/lose relationships.
    graph = defaultdict(list)

    # Define relationships
    graph["rock"].append("scissors")
    graph["scissors"].append("paper")
    graph["paper"].append("rock")

    return graph

def find_winner(option_graph, p0_choice, p1_choice):
    """using given directed graph of options and player choices, return
    winner's index, or none if tied"""
    if p1_choice in option_graph[p0_choice]:
        return 0
    elif p0_choice in option_graph[p1_choice]:
        return 1
    else:
        return None

def play_round():
    """primary game flow"""
    # initialize the list of options in this game
    options = ["rock", "paper", "scissors"]
    players = [Player("You"), Player("I")]

    # get users selection and store validated choice if possible
    user_choice = get_user_choice(options)
    computer_choice = get_computer_choice(options)

    print(f"\n{players[0]} chose: {user_choice}")
    print(f"{players[1]} chose: {computer_choice}!!\n")

    # Determine winner and respond appropriately
    options_graph = create_graph()
    windex = find_winner(options_graph,user_choice,computer_choice)
    
    print("Tie!" if windex is None else f"{players[windex].name} won!!")

while True:
    """main loop"""
    clear_screen()

    # welcome user and introduce game
    print("Hey, nice to see you!")
    print("\nLooks like you want to play a game of Rock, Paper, Scissors, eh?")
    print("I'm down. It's a very simple game, so I'll assume you know what")
    print("you're doing here.")

    play_round()

    # ask to play again
    play_again = input("\nPlay again? (y/n): ")

    # if done playing, say goodbye and close game
    if not play_again.lower().startswith("y"):
        input("\nWell, that was fun! See you around. (press enter)")
        clear_screen()
        break