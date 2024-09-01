# games.py

from gsclasses import *

class Pick_A_Number(BaseGame):
    def __init__(self, players:List[BasePlayer]) -> None:
        super().__init__(players)

    def play_game(self):
        import pick_a_number
        pick_a_number.play_game()

class Rock_Paper_Scissors(BaseGame):
    def __init__(self, players:List[BasePlayer]) -> None:
        super().__init__(players)

    def play_game(self):
        import rock_paper_scissors
        rock_paper_scissors.play_game()

class Tic_Tac_Toe(BaseGame):
    def __init__(self, players:List[BasePlayer]) -> None:
        super().__init__(players)

    def play_game(self):
        import tic_tac_toe
        tic_tac_toe.play_game()
