# rock_paper_scissors.py

import random
import time
from collections import defaultdict
import gsclasses as gsc
import gsutilities as gsu
from typing import Optional, List, Dict
from collections import OrderedDict

class RockPaperScissors(gsc.BaseGame):
    def __init__(self,
                 base_players: List[gsc.BasePlayer]) -> None:
        super().__init__(base_players)

        self.players: dict = self.setup_players()
        self.options_graph = self.create_options_graph()

    def setup_players(self) -> Dict[str, 'RockPaperScissors.Player']:
        """Creates player objects and returns them to call procedure."""
        return {"user": self.Player("You", "human", self),
                "opponent": self.Player("I", "computer", self, 0)}

    def create_options_graph(self) -> Dict[str, List[str]]:
        """Create directed graph to represent the win/lose relationship between
        options"""
        # TODO: Implement validation logic.
        graph = OrderedDict()

        # TODO: Make user configurable with persistent storage at the user level.
        graph["rock"] = []
        graph["paper"] = []
        graph["scissors"] = []

        graph["rock"].append("scissors")
        graph["paper"].append("rock")
        graph["scissors"].append("paper")

        return graph

    class Player(gsc.BasePlayer):
        """custom subclass for any game-specific functionality
        needed for the Player class."""
        def __init__(self,
                name: str,
                entity_type: str,
                game: 'RockPaperScissors',
                difficulty_level: Optional[int] = None) -> None:
            super().__init__(name, entity_type, difficulty_level)
        
            self.game = game
            self.selection: Optional[str] = None
            self.selection_raw_input: Optional[str] = None

        def make_selection(self) -> None:
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

        def get_choice_computer(self) -> str:
            """Generate a computer player's selection."""
            # TODO: implement more complex logic for computer selection:
            # 1. difficulty levels
            # 2. cheating
            # 3. prediction methods
            # 4. user specific decision-making based on user's trends
            # 5. selection strategies
            return random.choice(list(self.game.options_graph.keys()))

        def get_choice_user(self, retries: int = 3) -> str:
            """Collect the user's selection and parse/validate it."""
            if retries == 0:
                print("Too many invalid attempts. Read the instructions and try")
                print("again sometime.")

                raise ValueError("Too many failed attempts at making a selection.")

            self.game.rps_countdown()
            self.selection_raw_input = input("Choice?:").lower().strip()
            try:
                self.parse_user_selection()
                return self.selection
            except ValueError as e:
                print(f"Invalid input: {e}")
                return self.get_choice_user(retries - 1)
                        
        def parse_user_selection(self) -> None:
            """Parse user's input to identify the options that match and
            ensure that a unique selection is able to be determined."""
            matches = [
                option for option in self.game.options_graph.keys()
                if option.startswith(self.selection_raw_input)]

            if len(matches) == 1:
                self.selection = matches[0]
            elif len(matches) > 1:
                raise ValueError("multiple options match user input")
            else:
                raise ValueError("no options match user input")

    def play_game(self) -> None:
        while True:
            gsu.welcome_users_game("Rock, Paper, Scissors")
            
            try:
                self.get_player_selections()
                self.display_selections()
                self.resolve_round()
            except ValueError as e:
                print(f"{e}")

            if gsu.say_goodbye():
                break

    def get_player_selections(self) -> None:
        """Loops through players and initiates player selection choice for each"""
        for player in self.players.values():
            try:
                player.make_selection()
            except ValueError as e:
                raise ValueError(f"{e}")

    def display_selections(self) -> None:
        "Displays each player's selection after all selections have been made."
        for player in self.players.values():
            print(f"\n{player.name} chose: {player.selection}")

    def determine_round_winner(self) -> str:
        """using given directed graph of options and player choices, return
        winner's index, or none if tied"""
        if self.players["opponent"].selection in self.options_graph[self.players["user"].selection]:
            return "user"
        elif self.players["user"].selection in self.options_graph[self.players["opponent"].selection]:
            return "opponent"
        else:
            return None

    def resolve_round(self) -> None:
        """Finds the winner of the round and displays the results."""
        windex = self.determine_round_winner()
        if windex is None:
            print("Tie!")
        else:
            print(f"{self.players[windex].name} won!!")

    def rps_countdown(self) -> None:
        """countdown to player choice selection using traditional
        chant of "rock, paper, scissors" """
        for option in self.options_graph.keys():
            print(f"{option}...")
            time.sleep(0.5)
        print("\nShoot!!")