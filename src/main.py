from gsutilities import *
from gsclasses import *
from games import *

def welcome_user():
    clear_screen()
    print("Welcome to the Game Hub!")
   
def main():
    welcome_user()

    while True:
        game_choice = None
        try:
            game_choice = choose_game()
        except ValueError as e:
            print(f"\n{e}")        

        if game_choice is None:
            print("Please choose a game.")
        else:
            clear_screen()
            game_choice.play_game()
            clear_screen()

            print(f"\nWell, I hope that was a fun game.\n")

            if say_goodbye():        
                break
        
            clear_screen()

if __name__ == "__main__":
    main()
    clear_screen()