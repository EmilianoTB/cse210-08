import constants
from game.casting.actor import Actor
from game.shared.point import Point



class players(Actor):
    """
    Player one are you ready?.
    
    The objective of Player one is to move and destroy player 2 or vice versa.

    Each player's trail grows as they move. ---> 

    Players try to maneuver so the opponent collides with their trail. ----->

    If a player collides with their opponent's trail... ----> if you touch this "#" you will loose 

    we need to edit the keyboard keys for player 2 in this case Keyboard_services class 


    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, position, velocity):
        super().__init__()
        super().set_position(position)
        super().set_velocity(velocity)
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
        self.grow_tail(1)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments): 
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("8")
            segment.set_color(self.get_color())#change it , if not two players will have the same color
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = self.get_position().get_x() 
        y = self.get_position().get_y() 

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "0" if i == 0 else "#"
            #color = constants.RED if i == 0 else constants.RED
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self.get_color()) #In constants we have the colors
            self._segments.append(segment)