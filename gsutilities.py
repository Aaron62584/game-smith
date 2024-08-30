from os import system as os_sys, name as os_name

def clear_screen():
    """clears the console screen"""
    os_sys('cls' if os_name == 'nt' else 'clear')