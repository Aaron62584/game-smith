# gsclasses.py
from abc import ABC, abstractmethod
from typing import List

class BasePlayer:
    """Define basic player class with the minimum player characteristics and validation logic."""
    def __init__(self,
                 name: str,
                 entity_type: str,
                 difficulty_level: int | None = None
                 ) -> None:
        valid_entity_types = ["human", "computer"]
        
        if entity_type not in valid_entity_types:
            raise ValueError(f"Invalid entity type: {entity_type}. Valid options are {valid_entity_types}")

        self.name = name
        self.entity_type = entity_type

        if entity_type == "computer" and difficulty_level is None:
            raise ValueError("Difficulty level must be specified for computer players.")
        
        self.difficulty_level = difficulty_level

class BaseGame(ABC):
    """Define basic class from which specific games inherit."""
    def __init__(self, players:List[BasePlayer]) -> None:

        self.players = players
    
    # Define the abstract class methods that all derived games should implement.
    #@abstractmethod
    #def welcome_users():
    #    raise NotImplementedError