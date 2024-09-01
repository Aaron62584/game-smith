# tic_tac_toe.py

from gsclasses import *
from gsutilities import *
from typing import Optional, List

class Player(BasePlayer):
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
    welcome_users_game("Tic-Tac-Toe")
    raise NotImplementedError