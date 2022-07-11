from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Paddle(Actor):
    """A implement used to hit and bounce the ball in the game."""

    def __init__(self, body, image, debug = False):
        """Constructs a new Paddle.

        Args:Args:
            body: A new instance of Body.
            image: A new instance of image.
            debug: If it is being debugged.
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the paddle's body.

        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """
        Gets the paddle's body.

        Returns:
            An instance of Image.
        """
        return self._image

    def move_next(self):
        """Moves the paddle using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_up(self):
        """Steers the paddle up."""
        velocity = Point(0, -PADDLE_VELOCITY)
        self._body.set_velocity(velocity)

    def swing_down(self):
        """Steers the paddle down."""
        x = self._body.get_position().get_x()
        y = self._body.get_position().get_y()
        if y > (BALL_MAX_POINT_LOW):
            self._body.set_position(Point(x,BALL_MAX_POINT_LOW))
        velocity = Point(0, PADDLE_VELOCITY)
        self._body.set_velocity(velocity)
        

    def stop_moving(self):
        """Stops the paddle from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)