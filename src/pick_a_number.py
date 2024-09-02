# pick_a_number.py

import gsclasses as gsc
import gsutilities as gsu
from typing import Optional, List, Dict
import random

class PickANumber(gsc.BaseGame):
    def __init__(self,
                 base_players: List[gsc.BasePlayer]) -> None:
        super().__init__(base_players)

        self.players: dict = self.setup_players()
        self.number_selection_range = self.determine_number_selection_range()

    def setup_players(self) -> Dict[str, 'PickANumber.Player']:
        """Creates player objects and returns them to call procedure."""
        return {"guesser": self.Player("You", "human", self),
                "picker": self.Player("I", "computer", self, 0)}

    def determine_number_selection_range(self) -> Dict[str, int]:
        """Create dictionary with the min and max of the number
        selection range"""
        # TODO: Implement validation logic.
        # TODO: Make user configurable with persistent storage at the user level.
        return {"min": 1, "max": 10}

    class Player(gsc.BasePlayer):
        """custom subclass for any game-specific functionality
        needed for the Player class."""
        def __init__(self,
                name: str,
                entity_type: str,
                game: 'PickANumber', 
                difficulty_level: Optional[int] = None):
            super().__init__(name, entity_type, difficulty_level)
        
            self.game = game
            self.selection: Optional[int] = None
            self.selection_raw_input: Optional[str] = None

        def make_selection(self) -> None:
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

        def get_choice_computer(self) -> int:
            """Generate a computer player's selection."""
            # TODO: implement more complex logic for computer selection:
            # 1. difficulty levels
            # 2. cheating
            # 3. prediction methods
            # 4. user specific decision-making based on user's trends
            # 5. selection strategies
            return random.randint(self.game.number_selection_range['min'], self.game.number_selection_range['max'])

        def get_choice_user(self, retries: int = 3) -> int:
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
                return self.get_choice_user(retries - 1)
                        
        def parse_user_selection(self) -> None:
            """Parse user's input to identify the options that match and
            ensure that a unique selection is able to be determined."""
            user_choice = int(self.selection_raw_input)
            if isinstance(user_choice, int):
                if user_choice >= self.game.number_selection_range['min']:
                    if user_choice <= self.game.number_selection_range['max']:
                        self.selection = user_choice
                    else:
                        raise ValueError("Number too high.")
                else:
                    raise ValueError("Number too low.")
            else:
                raise ValueError("Value was not an integer.")

    def play_game(self) -> None:
        """main loop"""
        while True:
            gsu.welcome_users_game("Pick a Number")
            
            self.get_player_selections()
            self.display_selections()
            self.resolve_round()

            if gsu.say_goodbye():
                break
        
    def get_player_selections(self) -> None:
        """Loops through players and initiates player selection choice for each"""
        try:
            for player in self.players.values():
                player.make_selection()
        except ValueError as e:
            print(f"{e}")
            return

    def display_selections(self) -> None:
        "Displays each player's selection after all selections have been made."
        for player in self.players.values():
            print(f"\n{player.name} chose: {player.selection}")

    def determine_round_results(self) -> bool:
        """Determine if player correctly guessed number."""
        if self.players["guesser"].selection == self.players["picker"].selection:
            return True
        else:
            return False

    def resolve_round(self) -> None:
        """Finds the winner of the round and displays the results."""
        if self.determine_round_results():
            print(f"{self.players['guesser'].name} won!!")
        else:
            print(f"{self.players['picker'].name} won!!")