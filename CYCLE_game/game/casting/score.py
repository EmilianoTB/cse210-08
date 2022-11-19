from game.casting.actor import Actor 


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points=0
        self.add_points(0)
    
    def add_points(self, points):
        """
        Adds the given points if they move

        Args: 
            points (int): The pointas to add
        
        """

        self._points += points 
        self.set_text(f"Score: {self._points}")








    
    # def get_segments(self):
    #     """Gets the segments for each cycle.
    #     Returns:
    #     ---
    #         List: The list of actors for each cycle"""
    #     return self._segments

    # def get_name(self):
    #     """Gets the players name.
    #     Returns:
    #     ---
    #         String: The players name as text."""
    #     return self._name
