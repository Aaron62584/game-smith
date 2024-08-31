# rock_paper_scissors.py

import random
import time
from collections import defaultdict
from gsclasses import Player as BasicPlayer
from gsutilities import clear_screen
from typing import Optional

class Player(BasicPlayer):
    """custom subclass for any game-specific functionality
    needed for the Player class."""
    def __init__(self,
               name: str,
               entity_type: str,
               difficulty_level: Optional[int] = None):
        super().__init__(name, entity_type, difficulty_level)
    
        self.selection_raw_input = None
        self.selection = None

    def rps_countdown(self):
        """countdown to player choice selection using traditional
        chant of "rock, paper, scissors" """
        for option in options_graph.keys():
            print(f"{option}...")
            time.sleep(0.5)
        print("\nShoot!!")

    def make_selection(self):
        """Generate/collect this player's selection from available options."""
        if self.entity_type == "computer":
            self.selection = self.get_choice_computer()
        elif self.entity_type == "human":
            try:
                self.selection = self.get_choice_user()
            except ValueError as e:
                print(f"Game cancelled: {e}")
        else:
            raise ValueError(f"invalid entity_type for player: {self.name}")

    def get_choice_computer(self):
        """Generate a computer player's selection."""
        # TODO: implement more complex logic for computer selection:
        # 1. difficulty levels
        # 2. cheating
        # 3. prediction methods
        # 4. user specific decision-making based on user's trends
        # 5. selection strategies
        return random.choice(list(options_graph.keys()))

    def get_choice_user(self, retries=3):
        """Collect the user's selection and parse/validate it."""
        if retries == 0:
            print("Too many invalid attempts. Read the instructions and try")
            print("again sometime.")

            raise ValueError("Too many failed attempts at making a selection.")

        input("\nJust let me know when you're ready. (press enter)\n")

        self.rps_countdown()
        self.selection_raw_input = input().lower().strip()
        try:
            self.parse_user_selection()
            return self.selection
        except ValueError as e:
            print(f"Invalid input: {e}")
            self.get_choice_user(retries - 1)
                    
    def parse_user_selection(self):
        """Parse user's input to identify the options that match and
        ensure that a unique selection is able to be determined."""
        matches = [
            option for option in options_graph.keys()
              if option.startswith(self.selection_raw_input)]

        if len(matches) == 1:
            self.selection = matches[0]
        elif len(matches) > 1:
            raise ValueError("multiple options match user input")
        else:
            raise ValueError("no options match user input")

# TODO: Make options graph custom class to handle user configuration,
# retrieval, and storage.
def create_options_graph():
    """Create directed graph to represent the win/lose relationship between
    options"""
    # TODO: Implement validation logic.
    graph = defaultdict(list)

    # TODO: Make user configurable with persistent storage at the user level.
    graph["rock"].append("scissors")
    graph["scissors"].append("paper")
    graph["paper"].append("rock")

    return graph

def determine_round_winner(option_graph, players):
    """using given directed graph of options and player choices, return
    winner's index, or none if tied"""
    if players[1].selection in option_graph[players[0].selection]:
        return 0
    elif players[0].selection in option_graph[players[1].selection]:
        return 1
    else:
        return None

def setup_players():
    """Creates player objects and returns them to call procedure."""
    return [Player("You", "human"),
        Player("I", "computer", 0)]

def get_player_selections(players):
    """Loops through players and initiates player selection choice for each"""
    try:
        for player in players:
            player.make_selection()
    except ValueError as e:
        print(f"{e}")
        return

def display_selections(players):
    "Displays each player's selection after all selections have been made."
    for player in players:
        print(f"\n{player.name} chose: {player.selection}")

def resolve_round(players):
    """Finds the winner of the round and displays the results."""
    windex = determine_round_winner(options_graph,players)
    print("Tie!" if windex is None else f"{players[windex].name} won!!")

# TODO: Make a custom class for the rounds
def play_round():
    """Runs a round of the game."""
    players = setup_players()
    get_player_selections(players)
    display_selections(players)
    resolve_round(players)

options_graph = create_options_graph()

def main():
    while True:
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

if __name__ == "__main__":
    main()