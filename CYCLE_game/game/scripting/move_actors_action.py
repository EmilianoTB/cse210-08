from game.scripting.action import Action

class MoveActorsAction(Action):

    def execute(self, cast, script):
        """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    iterates through actors and call move_next()

    get actors - loop - call method move_next()
    """
        sets = cast.get_all_actors()

        for actor in sets:
            actor.move_next()
