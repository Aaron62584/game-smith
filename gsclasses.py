# gsclasses.py

class Player:
  """define player class"""
  def __init__(self,
               name: str,
               entity_type: str,
               difficulty_level: int | None = None):
    valid_entity_types = ["human", "computer"]

    if entity_type not in valid_entity_types:
        raise ValueError(f"Invalid entity type: {entity_type}. Valid options are {valid_entity_types}")

    self.name = name
    self.entity_type = entity_type

    if entity_type == "computer" and difficulty_level is None:
        raise ValueError("Difficulty level must be specified for computer players.")
    
    self.difficulty_level = difficulty_level

    