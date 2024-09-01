# pick_a_number.py

import random
from gsclasses import *
from gsutilities import *
from typing import Optional

def determine_number_selection_range():
    """Create dictionary with the min and max of the number
    selection range"""
    # TODO: Implement validation logic.
    # TODO: Make user configurable with persistent storage at the user level.
    return {"min": 1, "max": 10}

number_selection_range = determine_number_selection_range()

class Player(BasePlayer):
    """custom subclass for any game-specific functionality
    needed for the Player class."""
    def __init__(self,
               name: str,
               entity_type: str,
               difficulty_level: Optional[int] = None):
        super().__init__(name, entity_type, difficulty_level)
    
        self.selection: int = None
        self.selection_raw_input = None

    def make_selection(self):
        """Generate/collect this player's selection from available options."""
        if self.entity_type == "computer":
            self.selection = self.get_choice_computer()
        elif self.entity_type == "human":
            try:
                self.selection = self.get_choice_user()
            except ValueError as e:
                print(f"Game cancelled: Human player {self.name} wasn't able")
                print(f"to make a valid selection: {e}")
        else:
            raise ValueError(f"{self.name} seems to be neither a computer nor a human, somehow.")

    def get_choice_computer(self):
        """Generate a computer player's selection."""
        # TODO: implement more complex logic for computer selection:
        # 1. difficulty levels
        # 2. cheating
        # 3. prediction methods
        # 4. user specific decision-making based on user's trends
        # 5. selection strategies
        return random.randint(number_selection_range['min'], number_selection_range['max'])

    def get_choice_user(self, retries=3):
        """Collect the user's selection and parse/validate it."""
        if retries == 0:
            print("Too many invalid attempts. Read the instructions and try")
            print("again sometime.")

            raise ValueError("Too many failed attempts at making a selection.")

        self.selection_raw_input = input("What's your guess?").strip()
        try:
            self.parse_user_selection()
            return self.selection
        except ValueError as e:
            print(f"Invalid input: {e}")
            self.get_choice_user(retries - 1)
                    
    def parse_user_selection(self):
        """Parse user's input to identify the options that match and
        ensure that a unique selection is able to be determined."""
        user_choice = int(self.selection_raw_input)
        if isinstance(user_choice, int):
            if user_choice >= number_selection_range['min']:
                if user_choice <= number_selection_range['max']:
                    self.selection = user_choice
                else:
                    raise ValueError("Number too high.")
            else:
                raise ValueError("Number too low.")
        else:
            raise ValueError("Value was not an integer.")

def determine_round_results(players):
    """Determine if player correctly guessed number."""
    if players["guesser"].selection == players["picker"].selection:
        return True
    else:
        return False

def setup_players():
    """Creates player objects and returns them to call procedure."""
    return {"guesser": Player("You", "human"),
        "picker": Player("I", "computer", 0)}

def get_player_selections(players):
    """Loops through players and initiates player selection choice for each"""
    try:
        for player in players.values():
            player.make_selection()
    except ValueError as e:
        print(f"{e}")
        return

def display_selections(players):
    "Displays each player's selection after all selections have been made."
    for player in players.values():
        print(f"\n{player.name} chose: {player.selection}")

def resolve_round(players):
    """Finds the winner of the round and displays the results."""
    if determine_round_results(players):
        print(f"{players['guesser'].name} won!!")
    else:
        print(f"{players['picker'].name} won!!")

def play_round():
    """Runs a round of the game."""
    players = setup_players()
    get_player_selections(players)
    display_selections(players)
    resolve_round(players)

def play_game():
    """main loop"""
    while True:
        welcome_users_game("Pick a Number")
        play_round()

        if say_goodbye():
            break