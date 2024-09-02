from os import system as os_sys, name as os_name
from gsclasses import *
import games

def clear_screen():
    """clears the console screen"""
    os_sys('cls' if os_name == 'nt' else 'clear')

def welcome_users_game(game_name:str):
        # welcome user and introduce game
    print(f"Hey, nice to see you!")
    print(f"\nYou want to play {game_name}, eh?")
    print(f"I'm down. It's a very simple game, so I'll assume you know what")
    print(f"you're doing here.")

    input(f"\nLet me know when you're ready to go. (press enter)")  

def say_goodbye():
    # ask to play again
    play_again = input("\nPlay another game? (y/n): ")

    # if done playing, say goodbye and close game
    if play_again.lower().startswith("y"):
        return False
    else:
        input("\nWell, that was fun! See you around. (press enter)")
        return True

def choose_game():
    print("\nChoose a game to play:")
    print("1. Number Guessing Game")
    print("2. Rock, Paper, Scissors")
    print("3. Tic-Tac-Toe")
    choice = input("Enter the number of the game you want to play: ").strip()
    if choice == "1":
        from pick_a_number import PickANumber
        clear_screen()
        return PickANumber({"guesser": BasePlayer("You", "human"),
                            "picker": BasePlayer("I", "computer", 0)})
    elif choice == "2":
        from rock_paper_scissors import RockPaperScissors
        clear_screen()
        return RockPaperScissors({"User": BasePlayer("You", "human"),
                                  "Opponent": BasePlayer("I", "computer", 0)})
    elif choice == "3":
        from tic_tac_toe import TicTacToe
        clear_screen()
        return TicTacToe({"User": BasePlayer("You", "human"),
                          "Opponent": BasePlayer("I", "computer", 0)})
    else:
        raise ValueError(f"Invalid game selection.")
