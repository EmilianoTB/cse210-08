import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._message = Actor()
        self._x = int(constants.MAX_X / 2)
        self._y = int(constants.MAX_Y / 2)
        self._position = Point(self._x, self._y)

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            #self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player1 = cast.get_first_actor("player1")
        player2 = cast.get_first_actor("player2")
        #get the cast in actors function 
        cycle1 = player1.get_segments()[0]
        cycle2 = player2.get_segments()[0]
        #get cycle for each player 
        segments1 = player1.get_segments()[1:]
        segments2 = player2.get_segments()[1:]
        

        
        for segment1 in segments1: #SEARCH IF PLAYER 1 LOOSES 
            if cycle1.get_position().equals(segment1.get_position()):
                self._is_game_over = True
                self._message.set_text("YELLOW PLAYER 2 WON!")
                self._message.set_position(self._position)
                cast.add_actor("messages", self._message)

        for segment1 in segments2: 
            if cycle1.get_position().equals(segment1.get_position()):
                self._is_game_over = True
                self._message.set_text("YELLOW PLAYER 2 WON!")
                self._message.set_position(self._position)
                cast.add_actor("messages", self._message)


       
        for segment2 in segments2: #SEARCH IF PLAYER 2 LOOSES 
            if cycle2.get_position().equals(segment2.get_position()):
                self._is_game_over = True
                self._message.set_text("RED PLAYER 1 WON!")
                self._message.set_position(self._position)
                cast.add_actor("messages", self._message)



        for segment2 in segments1:
            if cycle2.get_position().equals(segment2.get_position()):
                self._is_game_over = True
                self._message.set_text("RED PLAYER 1 WON!")
                self._message.set_position(self._position)
                cast.add_actor("messages", self._message)


    
    # def _handle_segment_collision(self, cast):
    #     """Sets the game over flag if the snake collides with one of its segments.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     snake = cast.get_first_actor("snakes")
    #     head = snake.get_segments()[0]
    #     segments = snake.get_segments()[1:]
        
    #     for segment in segments:
    #         if head.get_position().equals(segment.get_position()):
    #             self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the PLAYERS IN COLOR WHITE if a player looses.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player1 = cast.get_first_actor("player1")
            player2 = cast.get_first_actor("player2")
            segments1 = player1.get_segments()
            segments2 = player2.get_segments()

            for segment1 in segments1:
                segment1.set_color(constants.WHITE)
            
            for segment2 in segments2:
                segment2.set_color(constants.WHITE)