from gsutilities import*

def main():
    clear_screen()
    print("Welcome to the Game Hub!")
    while True:
        try:
            print("\nChoose a game to play:")
            print("1. Number Guessing Game")
            print("2. Rock, Paper, Scissors")
            choice = input("Enter the number of the game you want to play: ").strip()
            if choice == "1":
                import pick_a_number
                pick_a_number.main()
            elif choice == "2":
                import rock_paper_scissors
                rock_paper_scissors.main()
            else:
                raise ValueError(f"Invalid game selection.")

            print(f"\nWell, I hope you had fun.\n")
        except ValueError as e:
            print(f"\n{e}")        


        play_again = input("\nWant to try another game? (y/n): ")
        if not play_again.lower().startswith("y"):
            break

    print("\nThanks for playing! See you next time.")

if __name__ == "__main__":
    main()
