from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MovePaddlesAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        paddles = cast.get_actors(PADDLE_GROUP)

        # PADDLE 1
        body1 = paddles[0].get_body()
        velocity1 = body1.get_velocity()
        position1 = body1.get_position()
        y1 = position1.get_y()
        position1 = position1.add(velocity1)

        # PADDLE 2
        body2 = paddles[1].get_body()
        velocity2 = body2.get_velocity()
        position2 = body2.get_position()
        y2 = position2.get_y()
        position2 = position2.add(velocity2)


        # PADDLE 1
        if y1 < 0:
            position1 = Point(position1.get_x(), 0)
        elif y1 > (SCREEN_HEIGHT - PADDLE_HEIGHT):
            position1 = Point(position1.get_x(), SCREEN_WIDTH - PADDLE_WIDTH)

        # PADDLE 2
        if y2 < 0:
            position2 = Point(position2.get_x(), 0)
        elif y2 > (SCREEN_HEIGHT - PADDLE_HEIGHT):
            position2 = Point(position2.get_x(), SCREEN_WIDTH - PADDLE_WIDTH)


        body1.set_position(position1)
        body2.set_position(position2)
        