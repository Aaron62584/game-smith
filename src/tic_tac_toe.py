# tic_tac_toe.py

import gsclasses as gsc
import gsutilities as gsu
from typing import Optional, List

class TicTacToe(gsc.BaseGame):
    def __init__(self, players:List[gsc.BasePlayer]) -> None:
        super().__init__(players)

    def play_game(self):
        import tic_tac_toe
        tic_tac_toe.play_game()

class Player(gsc.BasePlayer):
    """custom subclass for any game-specific functionality
    needed for the Player class."""
    def __init__(self,
               name: str,
               entity_type: str,
               difficulty_level: Optional[int] = None):
        super().__init__(name, entity_type, difficulty_level)

def print_board():
    """Prints the board in it's current state."""
    raise NotImplementedError

def setup_players():
    raise NotImplementedError

def play_game():
    gsu.welcome_users_game("Tic-Tac-Toe")
    raise NotImplementedError