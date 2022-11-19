import constants
from game.scripting.control_player1 import control_player1
from game.scripting.control_player2 import control_player2
#from game.casting.food import Food
from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.players import players
from game.scripting.script import Script
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    cast = Cast()
    y = int(constants.MAX_Y/8)
    x = int(constants.MAX_X/8)

    position = Point(x,constants.CELL_SIZE*50)
    velocity = Point(constants.CELL_SIZE*1,0)
    player1 = players(position,velocity)
    player1.set_color(constants.RED)
    cast.add_actor("player1", player1)
    
    position = Point(x,constants.CELL_SIZE*10)
    velocity = Point(-1 * constants.CELL_SIZE,0)
    player2 = players(position,velocity)
    player2.set_color(constants.YELLOW)
    cast.add_actor("player2", player2)

    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", control_player1(keyboard_service))
    script.add_action("input", control_player2(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()